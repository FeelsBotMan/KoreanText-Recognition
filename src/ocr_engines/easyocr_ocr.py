import easyocr
import numpy as np
from typing import Dict, Any
from . import OCREngine

class EasyOCREngine(OCREngine):
    def __init__(self, config: Dict[str, Any]):
        self.reader = easyocr.Reader(
            lang_list=config.get('lang_list', ['ko']),
            gpu=config.get('gpu', False)
        )

    def recognize(self, image: np.ndarray) -> str:
        try:
            result = self.reader.readtext(image)
            if not result:
                return ""
            
            # 인식된 모든 텍스트를 하나의 문자열로 결합
            text = ' '.join([item[1] for item in result])
            return text.strip()
        except Exception as e:
            print(f"EasyOCR 오류: {str(e)}")
            return ""

    def get_name(self) -> str:
        return "EasyOCR"
