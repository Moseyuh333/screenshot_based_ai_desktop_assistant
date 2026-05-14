import requests
from settings import store_key

DEFAULT_OPENAI_BASE_URL = "https://api.openai.com/v1"
DEFAULT_OPENAI_MODEL = "gpt-3.5-turbo"
REQUEST_TIMEOUT_SECONDS = 60
CLIENT_VERSION = "requests-v2"
MAX_RESPONSE_TOKENS = 700

def build_chat_completions_url(base_url):
    return f"{base_url.rstrip('/')}/chat/completions"

def extract_response_text(result):
    choices = result.get("choices") or []
    if not choices:
        return ""

    first_choice = choices[0] or {}
    message = first_choice.get("message") or {}

    for key in ("content", "reasoning_content", "text"):
        value = message.get(key) if isinstance(message, dict) else None
        if isinstance(value, str) and value.strip():
            return value.strip()

    value = first_choice.get("text")
    if isinstance(value, str) and value.strip():
        return value.strip()

    return ""

def send_prompt_to_chatgpt(prompt: str) -> str:
    api_key = store_key.load_api_key("ChatGPT")  # Load and decrypt
    if not api_key:
        return "API key not found."

    base_url = store_key.load_base_url("ChatGPT") or DEFAULT_OPENAI_BASE_URL
    endpoint = build_chat_completions_url(base_url)
    model_name = store_key.load_model_name("ChatGPT") or DEFAULT_OPENAI_MODEL
    print(f"LLM client: {CLIENT_VERSION}")
    print(f"LLM endpoint: {endpoint}")
    print(f"LLM model: {model_name}")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
        "max_tokens": MAX_RESPONSE_TOKENS,
    }

    try:
        response = requests.post(
            endpoint,
            headers=headers,
            json=data,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        if not response.ok:
            return f"API call failed: HTTP {response.status_code}: {response.text[:500]}"

        result = response.json()
        response_text = extract_response_text(result)
        if response_text:
            return response_text

        print(f"LLM raw response preview: {str(result)[:500]}")
        return f"API call failed: response did not contain text: {str(result)[:500]}"
    except Exception as e:
        return f"API call failed: {e}"
