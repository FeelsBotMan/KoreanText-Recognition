# KoreanText-Recognition
이 저장소는 여러 오픈소스 OCR 엔진의 한글 텍스트 인식 정확도를 비교하는 프로젝트입니다. 미리 준비된 한글 이미지 세트를 사용하여 각 엔진의 한글 인식 능력을 평가합니다. 이 프로젝트의 목표는 개발자가 한글 OCR 작업에 효과적인 도구를 선택하는 데 도움을 주는 종합적인 비교를 제공하는 것입니다.

## 목차
- 개요
- 기능
- 설치
- 사용법
- 평가된 OCR 엔진
- 결과
- 기여
- 라이센스
- OCR 엔진 요구사항
- 성능 최적화


## 개요
KoreanText-Recognition 프로젝트는 인기 있는 오픈소스 OCR 엔진의 한글 텍스트 인식 정확도를 비교하는 것을 목표로 합니다. 한글에 대한 OCR 솔루션 수요가 증가함에 따라 각 엔진의 강점과 약점을 이해하는 것이 중요합니다. 이 프로젝트는 한글 텍스트에 대한 OCR 엔진을 평가하고 비교하기 위한 표준화된 프레임워크를 제공합니다.

## 기능
- 다중 엔진 비교: 여러 오픈소스 OCR 엔진의 인식 정확도를 평가합니다.
- 미리 준비된 이미지 세트: 신뢰할 수 있는 비교를 위해 일관된 한글 이미지 세트를 사용합니다.
- 상세 정확도 지표: 각 엔진의 성능에 대한 인사이트를 제공하기 위해 정확도를 측정하고 보고합니다.

## 설치
이 저장소를 시작하려면 다음 단계를 따르세요:

1. 저장소를 클론합니다:
```
git clone https://github.com/yourusername/KoreanText-Recognition.git
cd KoreanText-Recognition
```
2. 필요한 종속성을 설치합니다:
```
pip install -r requirements.txt
```
3. OCR 엔진을 설치합니다. 일부 엔진은 추가 설정이 필요할 수 있으니, 공식 문서를 참조하세요.

### easyocr 설치

https://www.jaided.ai/easyocr/install/


### paddlepaddle 설치

https://github.com/PaddlePaddle/PaddleOCR/blob/main/doc/doc_en/quickstart_en.md#1-installation


### tesseract 설치

https://github.com/UB-Mannheim/tesseract/wiki


## 사용법
1. 테스트할 한글 이미지 파일을 images/ 디렉토리에 넣습니다.

```
images/
├── sample1.jpg
├── sample1.json
├── sample2.png
├── sample2.json
└── ...
```

JSON 파일의 형식은 다음과 같습니다:
```
{
    "text": "실제 이미지에 있는 텍스트 내용",
    "description": "이미지에 대한 설명(선택사항)"
}
```

2. 비교 스크립트를 실행합니다:
```
python src/main.py
```
3. 결과는 results/ 디렉토리에서 확인할 수 있습니다.

## 평가된 OCR 엔진
이번 프로젝트에서 평가되는 OCR 엔진은 다음과 같습니다:

- Tesseract OCR
- PaddleOCR
- EasyOCR

## 결과
결과 섹션에는 제공된 한글 이미지에 대한 각 OCR 엔진의 정확도 비교가 포함됩니다. 측정 항목은 다음과 같습니다:

- 인식 정확도: 올바르게 인식된 문자 비율.
- 오류율: 100자당 오류 수.
상세 결과는 results/에 저장됩니다.

## 기여
기여를 환영합니다! 다음 단계를 따르세요:

1. 저장소를 포크합니다.
2. 기능 추가 또는 버그 수정을 위한 새 브랜치를 만듭니다:
```
git checkout -b feature-name
```
3. 변경 사항을 커밋하고 포크에 푸시합니다.
4. 풀 리퀘스트를 제출합니다.
추가적인 OCR 엔진이나 지표가 포함될 경우 잘 문서화해 주세요.

## 라이센스
이 프로젝트는 MIT 라이센스에 따라 라이센스가 부여됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.

## OCR 엔진 요구사항

### Tesseract OCR
- 버전: 4.1.0 이상
- GPU 필요 여부: 불필요
- 최소 RAM: 4GB
- 추가 설치 요구사항:
  - Ubuntu: `sudo apt-get install tesseract-ocr tesseract-ocr-kor`
  - macOS: `brew install tesseract tesseract-lang`
  - Windows: [설치 프로그램](https://github.com/UB-Mannheim/tesseract/wiki)에서 다운로드

### PaddleOCR
- 버전: 2.6.0 이상
- GPU 지원: 선택사항 (CUDA 10.2+ 권장)
- 최소 RAM: 8GB
- 설치 방법:
  - GPU 버전: `pip install "paddlepaddle-gpu>=2.3.0"`
  - CPU 버전: `pip install "paddlepaddle>=2.3.0"`

### EasyOCR
- 버전: 1.6.2 이상
- GPU 지원: 선택사항 (CUDA 11.0+ 권장)
- 최소 RAM: 8GB
- 설치 방법:
  - GPU 버전: 
    ```bash
    pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu116
    pip install easyocr
    ```
  - CPU 버전:
    ```bash
    pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cpu
    pip install easyocr
    ```

## 성능 최적화
각 OCR 엔진은 하드웨어 리소스에 따라 다르게 구성할 수 있습니다:

### CPU 최적화
- Tesseract: 기본적으로 CPU에 최적화되어 있습니다.
- PaddleOCR: MKL-DNN 가속 및 멀티스레딩을 지원합니다.
- EasyOCR: CPU 모드에서도 작동하나, 처리 속도가 느릴 수 있습니다.

### GPU 최적화
- PaddleOCR: CUDA 지원으로 처리 속도가 크게 향상됩니다.
- EasyOCR: CUDA 지원으로 처리 속도가 크게 향상됩니다.
