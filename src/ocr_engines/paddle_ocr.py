from paddleocr import PaddleOCR
import numpy as np
from typing import Dict, Any
from . import OCREngine

class PaddleOCREngine(OCREngine):
    def __init__(self, config: Dict[str, Any]):
        self.ocr = PaddleOCR(
            lang=config.get('lang', 'korean'),
            use_gpu=config.get('use_gpu', False)
        )

    def recognize(self, image: np.ndarray) -> str:
        try:
            result = self.ocr.ocr(image, cls=False)
            if not result or not result[0]:
                return ""
            
            # 인식된 모든 텍스트를 하나의 문자열로 결합
            text = ' '.join([line[1][0] for line in result[0]])
            return text.strip()
        except Exception as e:
            print(f"PaddleOCR 오류: {str(e)}")
            return ""

    def get_name(self) -> str:
        return "PaddleOCR"
