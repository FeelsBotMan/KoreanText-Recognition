from typing import Dict, List
import numpy as np
import pandas as pd
from datetime import datetime
import os
import json

class MetricsCalculator:
    @staticmethod
    def calculate_accuracy(predicted: str, ground_truth: str) -> float:
        """
        텍스트 인식 정확도를 계산합니다.
        
        Args:
            predicted (str): OCR로 인식된 텍스트
            ground_truth (str): 실제 정답 텍스트
            
        Returns:
            float: 정확도 (0~1)
        """
        if not ground_truth:
            return 0.0
            
        correct_chars = sum(1 for p, g in zip(predicted, ground_truth) if p == g)
        total_chars = max(len(predicted), len(ground_truth))
        
        return correct_chars / total_chars if total_chars > 0 else 0.0

    @staticmethod
    def calculate_error_rate(predicted: str, ground_truth: str) -> float:
        """
        100자당 오류 수를 계산합니다.
        
        Args:
            predicted (str): OCR로 인식된 텍스트
            ground_truth (str): 실제 정답 텍스트
            
        Returns:
            float: 100자�� 오류 수
        """
        if not ground_truth:
            return 100.0
            
        errors = sum(1 for p, g in zip(predicted, ground_truth) if p != g)
        errors += abs(len(predicted) - len(ground_truth))
        
        return (errors * 100) / len(ground_truth)

    @staticmethod
    def save_results(results: Dict, save_path: str):
        """
        OCR 결과를 저장합니다.
        
        Args:
            results (Dict): OCR 결과 데이터
            save_path (str): 저장할 경로
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # JSON 형식으로 저장
        json_path = os.path.join(save_path, f'ocr_results_{timestamp}.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
            
        # CSV 형식으로 저장
        df = pd.DataFrame(results['detailed_results'])
        csv_path = os.path.join(save_path, f'ocr_results_{timestamp}.csv')
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
