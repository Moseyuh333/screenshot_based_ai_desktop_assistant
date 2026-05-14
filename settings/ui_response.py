import os

from PySide6 import QtWidgets, QtGui, QtCore

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICON_PATH = os.path.join(PROJECT_ROOT, "capture", "img", "arrow.ico")

class ResponsePopup(QtWidgets.QWidget):
    def __init__(self, message="Processing..."):
        super().__init__()
        self.setWindowTitle("Eclip AI")
        self.resize(560, 320)
        self.setMinimumSize(360, 180)
        self.setWindowIcon(QtGui.QIcon(ICON_PATH))
        self._drag_start = None
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.setWindowFlags(
            QtCore.Qt.Tool
            | QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        outer_layout = QtWidgets.QVBoxLayout(self)
        outer_layout.setContentsMargins(10, 10, 10, 10)

        self.panel = QtWidgets.QFrame()
        self.panel.setObjectName("responsePanel")
        self.panel.setStyleSheet(
            """
            QFrame#responsePanel {
                background-color: rgba(18, 24, 32, 218);
                border: 1px solid rgba(255, 255, 255, 70);
                border-radius: 10px;
            }
            QLabel#titleLabel {
                color: rgba(255, 255, 255, 230);
                font-size: 13px;
                font-weight: 600;
            }
            QPushButton#closeButton {
                color: white;
                background-color: rgba(255, 255, 255, 28);
                border: 1px solid rgba(255, 255, 255, 55);
                border-radius: 8px;
                min-width: 28px;
                min-height: 24px;
            }
            QPushButton#closeButton:hover {
                background-color: rgba(255, 255, 255, 45);
            }
            QTextEdit#responseText {
                color: rgba(255, 255, 255, 238);
                background-color: transparent;
                border: none;
                font-size: 14px;
                line-height: 1.35;
            }
            QScrollBar:vertical {
                background: transparent;
                width: 9px;
            }
            QScrollBar::handle:vertical {
                background: rgba(255, 255, 255, 80);
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0;
            }
            """
        )

        panel_layout = QtWidgets.QVBoxLayout(self.panel)
        panel_layout.setContentsMargins(16, 12, 16, 14)
        panel_layout.setSpacing(8)

        header_layout = QtWidgets.QHBoxLayout()
        self.title_label = QtWidgets.QLabel("Eclip AI")
        self.title_label.setObjectName("titleLabel")
        self.close_button = QtWidgets.QPushButton("X")
        self.close_button.setObjectName("closeButton")
        self.close_button.clicked.connect(self.close)
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.close_button)
        panel_layout.addLayout(header_layout)

        self.text_label = QtWidgets.QTextEdit()
        self.text_label.setObjectName("responseText")
        self.text_label.setReadOnly(True)
        self.text_label.setAcceptRichText(False)
        self.text_label.setText(message)
        panel_layout.addWidget(self.text_label)

        outer_layout.addWidget(self.panel)

        self.move_to_bottom_right()

        self.auto_close_timer = QtCore.QTimer(self)
        self.auto_close_timer.setSingleShot(True)

    def move_to_bottom_right(self):
        screen = QtWidgets.QApplication.primaryScreen()
        if not screen:
            return

        available = screen.availableGeometry()
        margin = 24
        x = available.right() - self.width() - margin
        y = available.bottom() - self.height() - margin
        self.move(max(available.left(), x), max(available.top(), y))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._drag_start = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_start is not None and event.buttons() & QtCore.Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_start)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_start = None
        event.accept()

    @QtCore.Slot()
    def show_processing(self):
        self.set_message("Processing...")
        self.resize(420, 180)
        self.move_to_bottom_right()
        self.show()

    @QtCore.Slot(str)
    def show_response(self, final_text):
        self.set_message(final_text or "No text extracted.")
        self.resize(560, 320)
        self.move_to_bottom_right()
        self.show()
        self.raise_()
        self.activateWindow()
        self.auto_close_timer.timeout.connect(self.close)
        self.auto_close_timer.start(45000)

    @QtCore.Slot(str)
    def set_message(self, message):
        self.text_label.setPlainText(message)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    popup = ResponsePopup()
    popup.set_message("Processing...")
    popup.show()

    def simulate_response():
        popup.set_message("Final response from API goes here.")
        popup.auto_close_timer.start(21000)

    QtCore.QTimer.singleShot(3000, simulate_response)

    sys.exit(app.exec())
