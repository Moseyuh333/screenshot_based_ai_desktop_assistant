"""
Google Gemini API Integration
Sends prompts to Google's Gemini API
"""
from settings import config, store_key
from generate.prompt import build_prompt

def send_to_gemini(extracted_text: str) -> str:
    """
    Send text to Gemini API for processing
    
    Args:
        extracted_text: Text extracted from screenshot
        
    Returns:
        Response from Gemini API or error message
    """
    try:
        import google.generativeai as genai
    except ImportError:
        return "Error: google-generativeai package not installed. Run: pip install google-generativeai"
    
    cfg = config.load_config()
    correction_mode = cfg.get("correction_mode", False)
    prompt = build_prompt(extracted_text, correction_mode)
    
    api_key = store_key.load_api_key("Gemini")
    if not api_key:
        return "API key not found. Please add your Gemini API key in Settings."
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        generation_config = {
            "temperature": 0.0,
            "max_output_tokens": 100,
        }
        
        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )
        return response.text.strip()
    except Exception as e:
        return f"Gemini API call failed: {e}"
