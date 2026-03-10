from send.llm_clients import ask_chatgpt
from send.llm_clients import ask_claude
from send.llm_clients import ask_gemini
from send.llm_clients import ask_custom

def dispatch_prompt(prompt: str, model: str = "chatgpt") -> str:
    """
    Dispatch the prompt to the selected AI model.
    :param prompt: Formatted prompt string.
    :param model: Target model name (chatgpt, claude, gemini, custom).
    :return: AI model's response or error string.
    """
    model_lower = model.lower()
    
    if model_lower == "chatgpt":
        return ask_chatgpt.send_to_chatgpt(prompt)
    elif model_lower == "claude":
        return ask_claude.send_to_claude(prompt)
    elif model_lower == "gemini":
        return ask_gemini.send_to_gemini(prompt)
    elif model_lower == "custom":
        return ask_custom.send_to_custom(prompt)
    else:
        return f"Invalid model selected: {model}"
