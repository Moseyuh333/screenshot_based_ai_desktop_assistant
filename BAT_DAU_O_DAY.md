# 🚀 HƯỚNG DẪN KHỞI ĐỘNG NHANH

## ⚠️ VẤN ĐỀ BẠN ĐANG GẶP PHẢI

**"Không trả lời ảnh tôi chụp"** → Do thiếu Tesseract OCR

---

## ✅ CÁCH SỬA (3 BƯỚC ĐƠN GIẢN)

### 📥 **Bước 1: Tải Tesseract OCR**

1. Mở link: https://github.com/UB-Mannheim/tesseract/wiki
2. Kéo xuống phần **"Windows"**
3. Click vào link màu xanh: **tesseract-ocr-w64-setup-5.5.0.20241111.exe**
4. File sẽ tải xuống (khoảng 60MB)

### 💾 **Bước 2: Cài Tesseract**

1. Chạy file vừa tải xuống
2. Khi hỏi path cài đặt → **GIỮ NGUYÊN** đường dẫn mặc định:
   ```
   C:\Program Files\Tesseract-OCR
   ```
3. Click **Next** → **Install**
4. Đợi cài xong → **Finish**

### 🎯 **Bước 3: Chạy Ứng Dụng**

Mở PowerShell trong thư mục này và chạy:

```powershell
python main.py
```

Hoặc click đúp vào file: `main.py`

---

## 🎮 CÁCH SỬ DỤNG

1. **Mở Settings API Key** (lần đầu):
   ```powershell
   python add_api_key.py
   ```
   - Chọn Model: ChatGPT/Claude/Gemini
   - Nhập API key
   - Click Save

2. **Chụp màn hình**: Nhấn `Ctrl + Alt + X`
3. **Chọn vùng** bằng chuột
4. **Đợi kết quả** - Popup sẽ hiện phản hồi từ AI

---

## 🔑 Lấy API Key Ở Đâu?

### ChatGPT (OpenAI) - KHUYÊN DÙNG
- 🔗 Link: https://platform.openai.com/settings/organization/api-keys
- 💰 Cần thêm $5-$10 vào tài khoản
- ⚡ Nhanh và chính xác

### Claude (Anthropic)
- 🔗 Link: https://console.anthropic.com/settings/keys
- 💰 $5 free credits cho người mới

### Gemini (Google)
- 🔗 Link: https://makersuite.google.com/app/apikey
- 🆓 Miễn phí (có giới hạn)

---

## 🛠️ TROUBLESHOOTING

### ❌ **Lỗi: "No OCR engine available"**
→ Bạn chưa cài Tesseract. Xem **Bước 1-2** ở trên.

### ❌ **Lỗi: "API key not found"**
→ Chạy: `python add_api_key.py` để thêm API key

### ❌ **Lỗi: "ModuleNotFoundError: No module named 'xxx'"**
→ Cài packages còn thiếu:
```powershell
python -m pip install pytesseract pillow PySide6 keyboard cryptography pystray openai anthropic google-generativeai requests
```

### ❌ **Popup không hiện**
→ Kiểm tra system tray (góc dưới bên phải màn hình), click chuột phải icon app

---

## 📂 CẤU TRÚC THƯ MỤC

```
screenshot_based_ai_desktop_assistant/
├── main.py                 ← Chạy file này
├── add_api_key.py          ← Thêm API key
├── CAI_DAT_TESSERACT.md    ← Hướng dẫn chi tiết OCR
├── HUONG_DAN_API_KEY.md    ← Hướng dẫn API key
├── capture/                ← Code chụp màn hình
├── generate/               ← Code tạo prompt
├── send/                   ← Code gọi LLM API
└── settings/               ← Config & API keys
```

---

## 💡 TIPS

- **Ctrl+Alt+X không hoạt động?** → Khởi động lại ứng dụng
- **Muốn đổi hotkey?** → Sửa trong `capture/snip_tool.py`
- **Response không chính xác?** → Bật "Correction Mode" trong Settings
- **Tesseract nhận diện kém?** → Chụp ảnh rõ nét hơn, hoặc cài PaddleOCR (khó hơn)

---

## 🎉 CHECKLIST SETUP

- [ ] Cài Tesseract OCR (Bước 1-2)
- [ ] Cài Python packages: `pip install -r requirements.txt`
- [ ] Thêm API key: `python add_api_key.py`
- [ ] Test chạy: `python main.py`
- [ ] Test chụp: Nhấn `Ctrl+Alt+X`

---

## ❓ CẦN HELP?

1. Đọc file `CAI_DAT_TESSERACT.md` - Hướng dẫn OCR chi tiết
2. Đọc file `HUONG_DAN_API_KEY.md` - Hướng dẫn API key chi tiết
3. Check logs trong terminal khi chạy `python main.py`

---

**Chúc bạn sử dụng thành công! 🎯**
