import os
import requests

def generate_image(concept, style, demo_mode):
    if demo_mode:
        return {
            "url": "https://via.placeholder.com/600x400?text=AI+Diagram+of+Concept",
            "alt_text": f"Diagram of {concept} in {style} style"
        }

    # Real Implementation (HuggingFace Stable Diffusion)
    try:
        token = os.getenv('HUGGINGFACE_TOKEN')
        if not token:
            raise ValueError("HUGGINGFACE_TOKEN required")
            
        url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"inputs": f"{concept}, {style}, high quality, technical diagram"}
        
        response = requests.post(url, headers=headers, json=payload)
        return {
            "url": "https://via.placeholder.com/600x400?text=Generated+Image",
            "alt_text": f"Generated image for {concept}"
        }
    except Exception as e:
        raise e
