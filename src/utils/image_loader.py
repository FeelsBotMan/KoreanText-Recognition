import os
from PIL import Image
import cv2
import numpy as np
import json
from typing import List, Tuple, Dict

class ImageLoader:
    @staticmethod
    def load_images_with_ground_truth(image_dir: str) -> List[Tuple[str, np.ndarray, str]]:
        """
        지정된 디렉토리에서 이미지와 정답 텍스트를 로드합니다.
        
        Args:
            image_dir (str): 이미지가 저장된 디렉토리 경로
            
        Returns:
            List[Tuple[str, np.ndarray, str]]: (이미지 파일명, 이미지 배열, 정답 텍스트) 튜플의 리스트
        """
        images = []
        valid_extensions = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')
        
        # 정답 데이터 로드
        ground_truth = {}
        for filename in os.listdir(image_dir):
            if filename.endswith('.json'):
                json_path = os.path.join(image_dir, filename)
                try:
                    with open(json_path, 'r', encoding='utf-8') as f:
                        image_name = os.path.splitext(filename)[0]
                        ground_truth[image_name] = json.load(f)['text']
                except Exception as e:
                    print(f"JSON 파일 로드 오류 ({filename}): {str(e)}")
        
        # 이미지 로드
        for filename in os.listdir(image_dir):
            if filename.lower().endswith(valid_extensions):
                image_name = os.path.splitext(filename)[0]
                if image_name not in ground_truth:
                    print(f"경고: {filename}에 대한 정답 텍스트가 없습니다.")
                    continue
                
                image_path = os.path.join(image_dir, filename)
                image = cv2.imread(image_path)
                if image is not None:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    images.append((filename, image, ground_truth[image_name]))
                    
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
