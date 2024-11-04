import os

# 기본 경로 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(BASE_DIR, 'images')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')

# OCR 엔진 요구사항 및 설정
ENGINE_REQUIREMENTS = {
    'tesseract': {
        'name': 'Tesseract OCR',
        'version': '>=4.1.0',
        'requires_gpu': False,
        'min_ram': '4GB',
        'additional_deps': [
            'tesseract-ocr',
            'tesseract-ocr-kor'
        ],
        'install_commands': {
            'ubuntu': 'sudo apt-get install tesseract-ocr tesseract-ocr-kor',
            'macos': 'brew install tesseract tesseract-lang',
            'windows': 'Download installer from https://github.com/UB-Mannheim/tesseract/wiki'
        }
    },
    'paddleocr': {
        'name': 'PaddleOCR',
        'version': '>=2.6.0',
        'requires_gpu': False,  # 선택사항
        'recommended_gpu': 'CUDA 10.2+',
        'min_ram': '8GB',
        'additional_deps': [
            'paddlepaddle-gpu',  # GPU 사용시
            'paddlepaddle'       # CPU 전용
        ],
        'install_commands': {
            'gpu': 'pip install "paddlepaddle-gpu>=2.3.0"',
            'cpu': 'pip install "paddlepaddle>=2.3.0"'
        }
    },
    'easyocr': {
        'name': 'EasyOCR',
        'version': '>=1.6.2',
        'requires_gpu': False,  # 선택사항
        'recommended_gpu': 'CUDA 11.0+',
        'min_ram': '8GB',
        'additional_deps': [
            'torch',
            'torchvision'
        ],
        'install_commands': {
            'gpu': 'pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu116',
            'cpu': 'pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cpu'
        }
    }
}

# OCR 엔진별 설정
TESSERACT_CONFIG = {
    'lang': 'kor',
    'config': '--psm 6'
}

PADDLEOCR_CONFIG = {
    'lang': 'korean',
    'use_gpu': False,
    'enable_mkldnn': True,  # CPU 성능 최적화
    'cpu_threads': 4        # CPU 스레드 수
}

EASYOCR_CONFIG = {
    'lang_list': ['ko'],
    'gpu': False,
    'model_storage_directory': os.path.join(BASE_DIR, 'models'),
    'download_enabled': True
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
