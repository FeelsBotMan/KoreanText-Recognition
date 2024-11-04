import os

# 기본 경로 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(BASE_DIR, 'images')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')

# OCR 엔진 설정
TESSERACT_CONFIG = {
    'lang': 'kor',
    'config': '--psm 6'
}

PADDLEOCR_CONFIG = {
    'lang': 'korean',
    'use_gpu': False
}

EASYOCR_CONFIG = {
    'lang_list': ['ko'],
    'gpu': False
}

# 결과 저장 설정
SAVE_DETAILED_RESULTS = True
SAVE_VISUALIZATIONS = True

# 평가 메트릭 설정
METRICS = {
    'accuracy': True,
    'error_rate': True,
    'processing_time': True
}
