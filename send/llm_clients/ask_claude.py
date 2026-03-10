"""
Claude API Integration
Sends prompts to Anthropic's Claude API
"""
from settings import config, store_key
from generate.prompt import build_prompt

def send_to_claude(extracted_text: str) -> str:
    """
    Send text to Claude API for processing
    
    Args:
        extracted_text: Text extracted from screenshot
        
    Returns:
        Response from Claude API or error message
    """
    try:
        import anthropic
    except ImportError:
        return "Error: anthropic package not installed. Run: pip install anthropic"
    
    cfg = config.load_config()
    correction_mode = cfg.get("correction_mode", False)
    prompt = build_prompt(extracted_text, correction_mode)
    
    api_key = store_key.load_api_key("Claude")
    if not api_key:
        return "API key not found. Please add your Claude API key in Settings."
    
    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=100,
            temperature=0.0,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text.strip()
    except Exception as e:
        return f"Claude API call failed: {e}"
