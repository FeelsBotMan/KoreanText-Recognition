import pytesseract
import numpy as np
from typing import Dict, Any
from . import OCREngine

class TesseractOCR(OCREngine):
    def __init__(self, config: Dict[str, Any]):
        self.lang = config.get('lang', 'kor')
        self.config = config.get('config', '--psm 6')

    def recognize(self, image: np.ndarray) -> str:
        try:
            text = pytesseract.image_to_string(
                image,
                lang=self.lang,
                config=self.config
            )
            return text.strip()
        except Exception as e:
            print(f"Tesseract OCR 오류: {str(e)}")
            return ""

    def get_name(self) -> str:
        return "Tesseract OCR"
