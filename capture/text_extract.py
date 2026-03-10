"""
Uses Tesseract OCR to extract and return text from an image.
Optimized for Windows with automatic Tesseract detection.
"""
import os
from PIL import Image

# Import Tesseract
try:
    import pytesseract
    
    # Set Tesseract path directly for Windows
    possible_paths = [
        r'C:\Program Files\Tesseract-OCR\tesseract.exe',
        r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
        os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Programs', 'Tesseract-OCR', 'tesseract.exe'),
    ]
    
    # Try to find and set Tesseract path
    tesseract_found = False
    for path in possible_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            tesseract_found = True
            print(f"✅ Using Tesseract OCR at: {path}")
            break
    
    # If not found in common paths, try PATH
    if not tesseract_found:
        try:
            import subprocess
            result = subprocess.run(['tesseract', '--version'], capture_output=True, check=True)
            tesseract_found = True
            print("✅ Using Tesseract from system PATH")
        except:
            pass
    
    if not tesseract_found:
        print("⚠️ Tesseract not found! Please install from: https://github.com/UB-Mannheim/tesseract/wiki")
        USE_TESSERACT = False
    else:
        USE_TESSERACT = True
        
except ImportError:
    print("⚠️ pytesseract not installed! Run: pip install pytesseract")
    USE_TESSERACT = False

def extract_text_from_image(image_path):
    """
    Extract text from image using Tesseract OCR.
    Returns extracted text as string.
    """
    if not USE_TESSERACT:
        error_msg = """❌ Tesseract OCR chưa được cài đặt!

📥 Cài Tesseract OCR:
1. Mở: https://github.com/UB-Mannheim/tesseract/wiki
2. Tải: tesseract-ocr-w64-setup-5.x.x.exe
3. Cài vào: C:\\Program Files\\Tesseract-OCR
4. Khởi động lại ứng dụng

Hoặc chạy: pip install pytesseract

📖 Xem chi tiết: CAI_DAT_TESSERACT.md"""
        return error_msg
    
    try:
        # Use Tesseract OCR
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='eng')
        extracted_text = text.strip()
        
        if not extracted_text:
            return "⚠️ Không phát hiện chữ trong ảnh. Thử chụp ảnh rõ hơn!"
        
        print(f"✅ OCR extracted: {len(extracted_text)} characters")
        return extracted_text
    
    except Exception as e:
        error_msg = f"""❌ Lỗi OCR: {str(e)}

💡 Giải pháp:
1. Kiểm tra Tesseract đã cài đúng: C:\\Program Files\\Tesseract-OCR
2. Xem hướng dẫn: CAI_DAT_TESSERACT.md
3. Thử chụp lại ảnh"""
        print(error_msg)
        return error_msg
