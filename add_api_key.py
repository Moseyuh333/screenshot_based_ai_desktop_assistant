"""
Script đơn giản để thêm API key trực tiếp
Chạy file này để mở cửa sổ Settings
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PySide6 import QtWidgets
from settings.ui_settings import SettingsWindow

if __name__ == "__main__":
    print("🔑 Mở cửa sổ Settings để thêm API key...")
    print("📝 Chọn AI Model và nhập API key của bạn")
    
    app = QtWidgets.QApplication(sys.argv)
    
    # Create settings window
    window = SettingsWindow()
    window.show()
    
    print("✅ Cửa sổ Settings đã mở!")
    print("💡 Sau khi Save, bạn có thể đóng cửa sổ này và chạy main.py")
    
    sys.exit(app.exec())
