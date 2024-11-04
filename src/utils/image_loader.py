import os
from PIL import Image
import cv2
import numpy as np
from typing import List, Tuple

class ImageLoader:
    @staticmethod
    def load_images(image_dir: str) -> List[Tuple[str, np.ndarray]]:
        """
        지정된 디렉토리에서 이미지를 로드합니다.
        
        Args:
            image_dir (str): 이미지가 저장된 디렉토리 경로
            
        Returns:
            List[Tuple[str, np.ndarray]]: (이미지 파일명, 이미지 배열) 튜플의 리스트
        """
        images = []
        valid_extensions = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')
        
        for filename in os.listdir(image_dir):
            if filename.lower().endswith(valid_extensions):
                image_path = os.path.join(image_dir, filename)
                image = cv2.imread(image_path)
                if image is not None:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    images.append((filename, image))
                    
        return images

    @staticmethod
    def preprocess_image(image: np.ndarray) -> np.ndarray:
        """
        OCR을 위한 이미지 전처리를 수행합니다.
        
        Args:
            image (np.ndarray): 입력 이미지
            
        Returns:
            np.ndarray: 전처리된 이미지
        """
        # 그레이스케일 변환
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        
        # 노이즈 제거
        denoised = cv2.fastNlMeansDenoising(gray)
        
        # 이진화
        _, binary = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        return binary
