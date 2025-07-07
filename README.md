# Screenshot-Based AI Desktop Assistant  
A fast, lightweight desktop tool that lets users instantly snip part of their screen, extract the visible text using OCR, and send it to an LLM of choice (OpenAI, Gemini, or Claude) for real-time responses — all without leaving their current window.

---

## Features

- **Region-Based Screenshot Capture** (Ctrl + Alt + X by default)  
- **LLM Integration** — Works with any OpenAI-compatible API (insert your key in settings)  
- **Text Extraction via OCR** using PaddleOCR  
- **Zero-distraction Popups** — Clean, borderless UI that appears over your current screen  
- **Lightweight and Fast** — Optimized for minimal resource usage  

---

## Tech Stack

| Component            | Technology Used          |
|---------------------|--------------------------|
| Programming Language| Python                   |
| OCR Engine          | PaddleOCR                |
| Screenshot Capture  | pyautogui, Pillow        |
| UI Toolkit          | tkinter                  |
| LLM Integration     | OpenAI / HTTP APIs       |
| Hotkeys             | keyboard                 |
| Config Persistence  | JSON                     |

---

## Project Structure
main.py — Entry point  
config.py — Stores API key and preferences  
snip_tool.py — Screenshot capture logic  
ocr_engine.py — Handles OCR using PaddleOCR  
ui_response.py — Popup logic (processing and response view)  
settings.json — Saves user API key and hotkey  
## Setup Instructions  
1. Clone the repo:  
git clone https://github.com/KatavinaNguyen/screenshot_based_ai_desktop_assistant.git  
cd screenshot_based_ai_desktop_assistant  
2. Install dependencies:  
pip install -r requirements.txt  
3. Run the app:  
python main.py  
4. Add your API key:  
Open the app’s settings panel and paste in your OpenAI or Gemini API key.  
You're now ready to use the screenshot hotkey (Ctrl + Alt + X).  
## Usage  
- Press Ctrl + Alt + X to snip a region of your screen  
- Text is automatically extracted using OCR  
- That text is sent to the selected LLM API  
- A lightweight popup appears with the LLM’s response  
- No screen dimming or disruption to your workflow  
## Skills Demonstrated  
- Python desktop app architecture  
- Real-time OCR with PaddleOCR  
- API communication with OpenAI-compatible LLMs  
- tkinter-based popup flow  
- Hotkey handling via `keyboard`  
- Modular codebase and async-safe popup flow  
- JSON-based config and settings persistence  
## Troubleshooting  
- OCR not working?  
Make sure PaddleOCR and dependencies are installed. Test `ocr_engine.py` directly if needed.  
- Popup not showing?  
Ensure no other tkinter windows are blocking. Restart the app.  
- Hotkey not working?  
Edit `settings.json` or use the app’s Settings menu to change the hotkey.  
- LLM not responding?  
Verify your API key and try a smaller text region. Ensure internet access.  
## Future Improvements  
- Support for multiple LLM providers via dropdown  
- Offline handwriting OCR  
- Local LLM backend (e.g., llama.cpp, Ollama)  
- Screenshot history log  
- More advanced UI using PyQt or Tauri  
## License  
MIT License — Free to use, modify, and share  
## Author  
Developed by [Katavina Nguyen](https://github.com/KatavinaNguyen)  
