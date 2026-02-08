from shared import get_nvidia_client, get_settings


def get_completion(prompt, model=None, temperature=0.7, max_tokens=None):
    """
    Helper function to get a completion from the NVIDIA API using OpenAI SDK.
    Useful for quick scripts and testing.
    """
    client = get_nvidia_client()
    settings = get_settings()

    response = client.chat.completions.create(
        model=model or settings.default_model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content
