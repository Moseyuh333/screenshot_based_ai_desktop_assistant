# 🔧 Sửa Lỗi OCR - Hướng Dẫn Cài Đặt Tesseract

## ⚠️ Vấn đề
PaddleOCR gặp lỗi **Windows Long Path** trên hệ thống của bạn. 
Tôi đã chuyển sang sử dụng **Tesseract OCR** (dễ cài hơn và ổn định hơn trên Windows).

---

## 📥 Cài Đặt Tesseract OCR

### **Bước 1: Tải Tesseract OCR cho Windows**

1. Mở link: https://github.com/UB-Mannheim/tesseract/wiki
2. Tải file: **tesseract-ocr-w64-setup-5.5.0.20241111.exe** (hoặc phiên bản mới nhất)
3. Chạy file installer
4. **Quan trọng**: Khi cài, chọn đường dẫn mặc định: `C:\Program Files\Tesseract-OCR`

### **Bước 2: Cài Python Package**

```powershell
python -m pip install pytesseract
```

### **Bước 3 (Nếu lỗi): Chỉnh Path**

Nếu vẫn báo lỗi "tesseract not found", mở file:
```
d:\New folder\screenshot_based_ai_desktop_assistant\capture\text_extract.py
```

Tìm dòng:
```python
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

Bỏ dấu `#` ở đầu dòng để uncomment.

---

## 🚀 Test Ứng Dụng

Sau khi cài Tesseract:

```powershell
python main.py
```

Nhấn **Ctrl+Alt+X** để chụp màn hình và test!

---

## 📊 So Sánh: Tesseract vs PaddleOCR

| Tính năng | Tesseract | PaddleOCR |
|-----------|-----------|-----------|
| **Cài đặt Windows** | ✅ Dễ | ❌ Khó (Long Path) |
| **Độ chính xác** | ⭐⭐⭐ Tốt | ⭐⭐⭐⭐⭐ Rất tốt |
| **Tốc độ** | ⚡ Nhanh | 🐢 Chậm hơn |
| **Khuyên dùng** | ✅ Windows | ✅ Linux/Mac |

---

## 🔗 Link Tải Tesseract
- **Windows**: https://github.com/UB-Mannheim/tesseract/wiki
- **Tài liệu**: https://tesseract-ocr.github.io/

---

## ✅ Kiểm Tra Tesseract Đã Cài

Chạy lệnh sau để kiểm tra:
```powershell
tesseract --version
```

Nếu hiện version → Đã cài thành công! 🎉
