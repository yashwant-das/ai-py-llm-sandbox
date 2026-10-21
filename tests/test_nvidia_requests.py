"""NVIDIA request, retrieval-mode, image, and setup regression tests."""

import base64
import contextlib
import io
import json
import os
from pathlib import Path
import runpy
import tempfile
import unittest
from unittest.mock import patch

import httpx
from openai import OpenAI
import requests

ROOT = Path(__file__).resolve().parents[1]
CHAT_SCRIPTS = [
    "fundamentals/model_basics.py",
    "fundamentals/streaming_responses.py",
    "fundamentals/temperature_sampling.py",
    "multimodal/vision_basics.py",
    "prompting/few_shot.py",
    "prompting/prompt_chaining.py",
    "prompting/structured_output.py",
    "prompting/zero_shot.py",
    "rag_embeddings/basic_rag.py",
    "safety/safety_demo.py",
    "setup/verify_setup.py",
    "tools_agents/function_calling.py",
]


class NvidiaRequestTests(unittest.TestCase):
    def run_demo(self, script, *, final_answer=True):
        captured = []
        clients = []

        def respond(request):
            body = json.loads(request.content)
            captured.append((request.url.path, body))
            if request.url.path.endswith("/embeddings"):
                return httpx.Response(
                    200,
                    json={
                        "object": "list",
                        "model": body["model"],
                        "data": [
                            {
                                "object": "embedding",
                                "index": i,
                                "embedding": [1.0, i + 1.0],
                            }
                            for i, _ in enumerate(body["input"])
                        ],
                    },
                )
            message = {
                "role": "assistant",
                "content": '{"name":"Jordan","experience_years":6,"skills":["Python"]}',
            }
            if any("setup-ok" in str(m.get("content")) for m in body["messages"]):
                message["content"] = "setup-ok" if final_answer else None
                if not final_answer:
                    message["reasoning"] = "Still thinking about the requested reply."
            if body.get("tools"):
                message = {
                    "role": "assistant",
                    "content": None,
                    "tool_calls": [
                        {
                            "id": "multiply-1",
                            "type": "function",
                            "function": {
                                "name": "multiply",
                                "arguments": '{"a":19,"b":7}',
                            },
                        }
                    ],
                }
            result = {
                "id": "test",
                "created": 0,
                "model": body["model"],
                "object": "chat.completion",
                "choices": [{"index": 0, "message": message, "finish_reason": "stop"}],
            }
            if body.get("stream"):
                result["object"] = "chat.completion.chunk"
                result["choices"] = [
                    {"index": 0, "delta": message, "finish_reason": None}
                ]
                return httpx.Response(
                    200,
                    headers={"content-type": "text/event-stream"},
                    text=f"data: {json.dumps(result)}\n\ndata: [DONE]\n\n",
                )
            return httpx.Response(200, json=result)

        def make_client(**kwargs):
            client = OpenAI(
                **kwargs,
                http_client=httpx.Client(transport=httpx.MockTransport(respond)),
            )
            clients.append(client)
            return client

        with tempfile.TemporaryDirectory() as directory:
            image = Path(directory) / "test.png"
            image.write_bytes(b"transport fixture")
            env = {
                "LLM_BASE_URL": "https://integrate.api.nvidia.com/v1",
                "LLM_API_KEY": "test",
                "LLM_MODEL_ID": "nvidia/nemotron-3.5-lightning-30b-a3b",
                "LLM_VISION_MODEL": "meta/llama-3.2-11b-vision-instruct",
                "LLM_EMBEDDING_MODEL": "nvidia/nemotron-3-embed-1b",
                "VISION_IMAGE_PATH": str(image),
            }
            stdout = io.StringIO()
            code = 0
            try:
                with (
                    patch.dict(os.environ, env, clear=True),
                    patch("dotenv.load_dotenv"),
                    patch("openai.OpenAI", make_client),
                    contextlib.redirect_stdout(stdout),
                ):
                    try:
                        runpy.run_path(
                            str(ROOT / "src/genai_playground" / script),
                            run_name="__main__",
                        )
                    except SystemExit as exc:
                        code = exc.code or 0
            finally:
                for client in clients:
                    client.close()
        return captured, stdout.getvalue(), code

    def test_short_chat_budgets_disable_thinking_including_streams_and_tool_followups(
        self,
    ):
        for script in CHAT_SCRIPTS:
            if script == "multimodal/vision_basics.py":
                continue
            with self.subTest(script=script):
                calls, _, code = self.run_demo(script)
                self.assertEqual(code, 0)
                chat = [
                    body for path, body in calls if path.endswith("/chat/completions")
                ]
                self.assertTrue(chat)
                for body in chat:
                    self.assertEqual(
                        body.get("chat_template_kwargs"), {"enable_thinking": False}
                    )
                    self.assertNotIn("reasoning_effort", body)

    def test_vision_does_not_send_unsupported_thinking_options(self):
        calls, _, code = self.run_demo("multimodal/vision_basics.py")
        self.assertEqual(code, 0)
        self.assertNotIn("chat_template_kwargs", calls[0][1])
        self.assertNotIn("reasoning_effort", calls[0][1])

    def test_retrieval_embeds_documents_and_query_in_separate_modes(self):
        for script in [
            "rag_embeddings/embeddings_basics.py",
            "rag_embeddings/basic_rag.py",
        ]:
            with self.subTest(script=script):
                calls, _, code = self.run_demo(script)
                self.assertEqual(code, 0)
                embeddings = [
                    body for path, body in calls if path.endswith("/embeddings")
                ]
                self.assertEqual(len(embeddings), 2)
                self.assertEqual(embeddings[0].get("input_type"), "passage")
                self.assertEqual(len(embeddings[0]["input"]), 3)
                self.assertEqual(embeddings[1].get("input_type"), "query")
                self.assertEqual(len(embeddings[1]["input"]), 1)

    def test_setup_rejects_reasoning_without_a_final_answer(self):
        _, output, code = self.run_demo("setup/verify_setup.py", final_answer=False)
        self.assertEqual(code, 1)
        self.assertIn("Connection test: FAILED", output)


class NvidiaImageTests(unittest.TestCase):
    def load_demo(self, model="black-forest-labs/flux.1-dev"):
        env = {
            "LLM_BASE_URL": "https://integrate.api.nvidia.com/v1",
            "LLM_API_KEY": "test",
            "LLM_IMAGE_BASE_URL": "https://ai.api.nvidia.com/v1/genai",
            "LLM_IMAGE_MODEL": model,
        }
        with patch.dict(os.environ, env, clear=True), patch("dotenv.load_dotenv"):
            return runpy.run_path(
                str(ROOT / "src/genai_playground/multimodal/image_generation.py")
            )

    def test_image_uses_nvidia_route_and_decodes_artifact(self):
        demo = self.load_demo()
        png = base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jRZkAAAAASUVORK5CYII="
        )

        def respond(url, **kwargs):
            self.assertEqual(
                url,
                "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-dev",
            )
            self.assertEqual(kwargs["json"]["prompt"], "A red square")
            self.assertEqual(kwargs["json"]["steps"], 20)
            self.assertEqual(kwargs["json"]["cfg_scale"], 5)
            response = requests.Response()
            response.status_code = 200
            response._content = json.dumps(
                {
                    "artifacts": [
                        {
                            "base64": base64.b64encode(png).decode(),
                            "finishReason": "SUCCESS",
                        }
                    ]
                }
            ).encode()
            return response

        with (
            patch("requests.post", respond),
            patch(
                "httpx.Client.send",
                side_effect=AssertionError("Use the NVIDIA image route"),
            ),
        ):
            self.assertEqual(demo["generate_image"]("A red square"), png)

    def test_provider_error_does_not_generate_a_fake_image(self):
        demo = self.load_demo()

        def reject(*args, **kwargs):
            response = requests.Response()
            response.status_code = 404
            response._content = b"{}"
            return response

        with (
            patch("requests.post", reject),
            patch(
                "httpx.Client.send",
                side_effect=AssertionError("Use the NVIDIA image route"),
            ),
            contextlib.redirect_stdout(io.StringIO()),
        ):
            self.assertIsNone(demo["generate_image"]("A red square"))


if __name__ == "__main__":
    unittest.main()
