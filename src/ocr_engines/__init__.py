from abc import ABC, abstractmethod
import numpy as np
from typing import Dict, Any

class OCREngine(ABC):
    @abstractmethod
    def __init__(self, config: Dict[str, Any]):
        """OCR 엔진을 초기화합니다."""
        pass

    @abstractmethod
    def recognize(self, image: np.ndarray) -> str:
        """이미지에서 텍스트를 인식합니다."""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """엔진의 이름을 반환합니다."""
        pass
