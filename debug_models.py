import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.absolute()))

# Now we can import shared
try:
	from shared import get_nvidia_client
except ImportError:
	# Fallback if running from root without package install
	sys.path.append(".")
	from shared import get_nvidia_client

def list_models():
    try:
        client = get_nvidia_client()
        response = client.models.list()
        
        print("Available Image Models:")
        image_keywords = ["stable", "flux", "image", "diffusion", "sdxl"]
        found = False
        for model in response:
             # Check for the specific model the user requested too
             if any(k in model.id.lower() for k in image_keywords) or "3.5" in model.id:
                 print(f" - {model.id}")
                 found = True
        
        if not found:
            print("No image generation models found in the list.")
            
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_models()
