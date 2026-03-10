# 🔑 Hướng Dẫn Thêm API Key

## Cách 1: Sử dụng System Tray (Khay hệ thống)

1. **Tìm icon của ứng dụng** trong system tray (góc dưới bên phải màn hình Windows)
   - Tìm icon của Eclip AI
   - Nếu không thấy, click vào mũi tên "^" để hiển thị các icon ẩn

2. **Click chuột phải** vào icon Eclip AI

3. Chọn **"Settings"** từ menu

4. Cửa sổ Settings sẽ hiện ra với các tùy chọn:
   - **AI Model**: Chọn ChatGPT, Claude, hoặc Gemini
   - **API Key**: Nhập API key của bạn
   - **Correction Mode**: Bật/tắt chế độ sửa lỗi văn bản

5. **Nhập API Key**:
   - Chọn AI model bạn muốn sử dụng
   - Click nút **"Get Key"** để mở trang web lấy API key
   - Copy API key và paste vào ô "API Key"
   - Click **"Save"** để lưu

---

## Cách 2: Chạy Demo Settings (Nếu ứng dụng chính gặp vấn đề)

Nếu không mở được Settings từ system tray, bạn có thể chạy trực tiếp:

```powershell
python test/demo_ui_settings.py
```

---

## 🔗 Nơi Lấy API Key

### **ChatGPT (OpenAI)**
- Link: https://platform.openai.com/settings/organization/api-keys
- Yêu cầu: Tạo tài khoản OpenAI và thêm phương thức thanh toán

### **Claude (Anthropic)**
- Link: https://console.anthropic.com/settings/keys
- Yêu cầu: Tạo tài khoản Anthropic và thêm credits

### **Gemini (Google)**
- Link: https://makersuite.google.com/app/apikey
- Yêu cầu: Tài khoản Google

---

## ⚙️ Cấu hình hiện tại

File config được lưu tại: `settings/config.json`

Để xem cấu hình hiện tại:
```powershell
Get-Content settings/config.json
```

---

## 🛠️ Sửa lỗi System Tray Icon

Nếu không thấy icon trong system tray, có thể icon bị thiếu. Chạy lệnh sau để tạo icon mặc định:

```powershell
# Icon đã có sẵn tại: capture/img/arrow.png
# Nếu không hiển thị, thử chạy lại ứng dụng
```

---

## ✅ Kiểm Tra API Key Đã Lưu

Sau khi lưu API key, bạn có thể kiểm tra:

1. Mở file `settings/config.json`
2. Tìm phần `"api_keys"` - API key sẽ được mã hóa (encrypted)
3. Trường `"selected_model"` cho biết model đang sử dụng

---

## 🚀 Sử Dụng

Sau khi thêm API key:

1. **Chụp màn hình**: Nhấn `Ctrl + Alt + X`
2. **Chọn vùng** cần OCR bằng chuột
3. **Đợi xử lý**: OCR + LLM sẽ phân tích văn bản
4. **Xem kết quả**: Popup hiển thị phản hồi từ AI

---

## 💡 Lưu Ý

- API key được mã hóa và lưu cục bộ trên máy bạn
- Mỗi lần gọi API sẽ tốn phí (tùy nhà cung cấp)
- Correction Mode: Chế độ sửa lỗi chính tả thay vì trả lời câu hỏi
- Nếu gặp lỗi "API key not found", kiểm tra lại Settings
