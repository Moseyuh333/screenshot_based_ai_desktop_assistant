"""
Uses PaddleOCR to extract and return text from an image (user's screenshot, returns to snip_tool.py).
"""
import logging

logging.getLogger("ppocr").setLevel(logging.ERROR)  # Suppress noisy PaddleOCR logs

def extract_text_from_image(image_path):
    try:
        from paddleocr import PaddleOCR
    except ModuleNotFoundError as e:
        if e.name == "paddle":
            raise RuntimeError(
                "OCR dependency missing: install paddlepaddle in your .venv, then restart the app."
            ) from e
        raise

    ocr = PaddleOCR(use_angle_cls=True, lang="en", show_log=False)
    result = ocr.ocr(image_path, cls=True)

    extracted_text_list = []
    if result and result[0]:
        for line in result[0]:
            text = line[1][0]
            extracted_text_list.append(text)

    return "\n".join(extracted_text_list)
