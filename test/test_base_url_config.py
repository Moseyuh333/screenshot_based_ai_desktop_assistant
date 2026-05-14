import os
import tempfile
import sys
import types
import unittest

cryptography_module = types.ModuleType("cryptography")
fernet_module = types.ModuleType("cryptography.fernet")
requests_module = types.ModuleType("requests")


class FakeFernet:
    def __init__(self, key):
        self.key = key

    def encrypt(self, value):
        return b"encrypted:" + value

    def decrypt(self, value):
        prefix = b"encrypted:"
        if not value.startswith(prefix):
            raise ValueError("Invalid fake encrypted value")
        return value[len(prefix):]


fernet_module.Fernet = FakeFernet
sys.modules.setdefault("cryptography", cryptography_module)
sys.modules.setdefault("cryptography.fernet", fernet_module)
sys.modules.setdefault("requests", requests_module)

from settings import store_key
from send.llm_clients import ask_chatgpt


class BaseUrlConfigTests(unittest.TestCase):
    def setUp(self):
        self.original_config_file = store_key.CONFIG_FILE
        self.temp_dir = tempfile.TemporaryDirectory()
        store_key.CONFIG_FILE = os.path.join(self.temp_dir.name, "config.json")

    def tearDown(self):
        store_key.CONFIG_FILE = self.original_config_file
        self.temp_dir.cleanup()

    def test_saves_normalized_base_url(self):
        store_key.save_user_settings(
            model="ChatGPT",
            api_key="dummy-test-key",
            base_url=" https://api.zunef.space/v1/ ",
            model_name=" openai/gpt-oss-120b ",
        )

        self.assertEqual(
            store_key.load_base_url("ChatGPT"),
            "https://api.zunef.space/v1",
        )
        self.assertEqual(
            store_key.load_model_name("ChatGPT"),
            "openai/gpt-oss-120b",
        )

    def test_empty_api_key_keeps_existing_key(self):
        store_key.save_user_settings(
            model="ChatGPT",
            api_key="dummy-existing-key",
            base_url="https://api.openai.com/v1",
            model_name="gpt-3.5-turbo",
        )
        store_key.save_user_settings(
            model="ChatGPT",
            api_key="",
            base_url="https://api.zunef.space/v1",
            model_name="openai/gpt-oss-120b",
        )

        self.assertEqual(store_key.load_api_key("ChatGPT"), "dummy-existing-key")
        self.assertEqual(
            store_key.load_base_url("ChatGPT"),
            "https://api.zunef.space/v1",
        )
        self.assertEqual(
            store_key.load_model_name("ChatGPT"),
            "openai/gpt-oss-120b",
        )

    def test_chatgpt_client_uses_saved_base_url(self):
        captured = {}

        class FakeResponse:
            ok = True
            status_code = 200
            text = ""

            def raise_for_status(self):
                return None

            def json(self):
                return {"choices": [{"message": {"content": "ok"}}]}

        def fake_post(url, headers, json, timeout):
            captured["url"] = url
            captured["headers"] = headers
            captured["json"] = json
            captured["timeout"] = timeout
            return FakeResponse()

        requests_module.post = fake_post
        store_key.save_user_settings(
            model="ChatGPT",
            api_key="dummy-test-key",
            base_url="https://api.zunef.space/v1/",
            model_name="openai/gpt-oss-120b",
        )

        self.assertEqual(ask_chatgpt.send_prompt_to_chatgpt("hello"), "ok")
        self.assertEqual(captured["url"], "https://api.zunef.space/v1/chat/completions")
        self.assertEqual(captured["headers"]["Authorization"], "Bearer dummy-test-key")
        self.assertEqual(captured["headers"]["Content-Type"], "application/json")
        self.assertEqual(
            captured["json"]["messages"],
            [{"role": "user", "content": "hello"}],
        )
        self.assertEqual(captured["json"]["model"], "openai/gpt-oss-120b")
        self.assertEqual(captured["json"]["temperature"], 0.0)
        self.assertEqual(captured["json"]["max_tokens"], 700)
        self.assertEqual(captured["timeout"], 60)

    def test_chatgpt_client_handles_empty_content(self):
        class FakeResponse:
            ok = True
            status_code = 200
            text = ""

            def json(self):
                return {"choices": [{"message": {"content": None}}]}

        requests_module.post = lambda *args, **kwargs: FakeResponse()
        store_key.save_user_settings(
            model="ChatGPT",
            api_key="dummy-test-key",
            base_url="https://api.zunef.space/v1/",
            model_name="openai/gpt-oss-120b",
        )

        response = ask_chatgpt.send_prompt_to_chatgpt("hello")
        self.assertIn("response did not contain text", response)


if __name__ == "__main__":
    unittest.main()
