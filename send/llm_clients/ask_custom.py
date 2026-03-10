"""
Custom/OpenAI-compatible API Integration
Allows using any OpenAI-compatible API endpoint
"""
from settings import config, store_key
from generate.prompt import build_prompt
import requests

def send_to_custom(extracted_text: str, api_url: str = None) -> str:
    """
    Send text to a custom OpenAI-compatible API endpoint
    
    Args:
        extracted_text: Text extracted from screenshot
        api_url: Custom API endpoint URL
        
    Returns:
        Response from custom API or error message
    """
    cfg = config.load_config()
    correction_mode = cfg.get("correction_mode", False)
    prompt = build_prompt(extracted_text, correction_mode)
    
    api_key = store_key.load_api_key("Custom")
    if not api_key:
        return "API key not found. Please add your Custom API key in Settings."
    
    if not api_url:
        api_url = cfg.get("custom_api_url", "http://localhost:11434/v1/chat/completions")
    
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        data = {
            "model": cfg.get("custom_model", "gpt-3.5-turbo"),
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
            "max_tokens": 100
        }
        
        response = requests.post(api_url, json=data, headers=headers, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Custom API call failed: {e}"
