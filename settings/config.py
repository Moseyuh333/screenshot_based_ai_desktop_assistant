from .store_key import load_config, load_api_key, load_base_url, load_model_name

def get_selected_model():
    config = load_config()
    return config.get("selected_model", "chatgpt")  # default fallback

def get_correction_mode():
    config = load_config()
    return config.get("correction_mode", False)

def get_api_key(model=None):
    from .store_key import load_api_key
    model = model or get_selected_model()
    return load_api_key(model)

def get_base_url(model=None):
    from .store_key import load_base_url
    model = model or get_selected_model()
    return load_base_url(model)

def get_model_name(model=None):
    from .store_key import load_model_name
    model = model or get_selected_model()
    return load_model_name(model)
