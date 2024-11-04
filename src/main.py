import os
import time
from typing import Dict, List
import json

from config import *
from utils.image_loader import ImageLoader
from utils.metrics import MetricsCalculator
from ocr_engines.tesseract_ocr import TesseractOCR
from ocr_engines.paddle_ocr import PaddleOCREngine
#from ocr_engines.easyocr_ocr import EasyOCREngine

def initialize_engines() -> List:
    """OCR 엔진들을 초기화합니다."""
    engines = [
        TesseractOCR(TESSERACT_CONFIG),
        PaddleOCREngine(PADDLEOCR_CONFIG),
        #EasyOCREngine(EASYOCR_CONFIG)
    ]
    return engines

def process_images(engines: List, image_dir: str, results_dir: str):
    """이미지를 처리하고 결과를 저장합니다."""
    # 결과 디렉토리 생성
    os.makedirs(results_dir, exist_ok=True)
    
    # 이미지와 정답 텍스트 로드
    images = ImageLoader.load_images_with_ground_truth(image_dir)
    
    results = {
        'summary': {},
        'detailed_results': []
    }
    
    for engine in engines:
        engine_name = engine.get_name()
        print(f"\n{engine_name} 처리 중...")
        
        engine_results = {
            'name': engine_name,
            'total_time': 0,
            'total_accuracy': 0,
            'total_error_rate': 0,
            'processed_images': 0
        }
        
        for filename, image, ground_truth in images:
            # 이미지 전처리
            processed_image = ImageLoader.preprocess_image(image)
            
            # OCR 수행 및 시간 측정
            start_time = time.time()
            recognized_text = engine.recognize(processed_image)
            processing_time = time.time() - start_time
            
            # 정확도와 오류율 계산
            accuracy = MetricsCalculator.calculate_accuracy(recognized_text, ground_truth)
            error_rate = MetricsCalculator.calculate_error_rate(recognized_text, ground_truth)
            
            # 결과 저장
            result_entry = {
                'engine': engine_name,
                'filename': filename,
                'recognized_text': recognized_text,
                'ground_truth': ground_truth,
                'accuracy': accuracy,
                'error_rate': error_rate,
                'processing_time': processing_time
            }
            
            results['detailed_results'].append(result_entry)
            engine_results['total_time'] += processing_time
            engine_results['total_accuracy'] += accuracy
            engine_results['total_error_rate'] += error_rate
            engine_results['processed_images'] += 1
        
        # 평균 계산
        if engine_results['processed_images'] > 0:
            engine_results['avg_accuracy'] = engine_results['total_accuracy'] / engine_results['processed_images']
            engine_results['avg_error_rate'] = engine_results['total_error_rate'] / engine_results['processed_images']
            engine_results['avg_time'] = engine_results['total_time'] / engine_results['processed_images']
        
        # 엔진별 요약 정보 저장
        results['summary'][engine_name] = engine_results
    
    # 결과 저장
    MetricsCalculator.save_results(results, results_dir)

def main():
    """메인 함수"""
    print("한글 OCR 엔진 비교 시작...")
    
    # OCR 엔진 초기화
    engines = initialize_engines()
    
    # 이미지 처리 및 결과 저장
    process_images(engines, IMAGE_DIR, RESULTS_DIR)
    
    print("\n처리 완료! 결과는 results 디렉토리에서 확인할 수 있습니다.")

if __name__ == "__main__":
    main()
