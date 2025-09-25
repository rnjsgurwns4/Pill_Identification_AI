# Pill_Identification_AI
2025년 2학기 종합설계 7조

💊 AI 알약 식별 프로젝트 (Pill Identifier AI)
이미지 한 장으로 알약의 모양, 색상, 각인(글자)을 종합적으로 분석하여 어떤 약인지 식별해주는 AI 기반 시스템입니다.

(실제 프로젝트 실행 화면 예시)

✨ 주요 기능
🧠 다중 객체 탐지: 한 이미지에 여러 개의 알약이 있어도 YOLOv8 모델이 각각의 위치를 정확하게 탐지합니다.

🎨 정교한 특징 추출:

모양: 직접 학습시킨 TensorFlow/Keras 모델을 통해 원형, 타원형 등 알약의 형태를 분류합니다.

색상: K-Means 클러스터링 알고리즘으로 배경이 제거된 이미지에서 가장 지배적인 색상을 추출합니다.

각인: Tesseract OCR 및 Naver CLOVA OCR을 활용, 다양한 전처리 기법을 적용하여 알약 표면의 글자나 숫자를 인식합니다.

🔍 데이터베이스 매칭: 추출된 특징(모양, 색상, 각인)을 종합하여 데이터베이스와 비교하고, 가장 유사한 알약 후보를 점수와 함께 제시합니다.

🌐 웹 API 제공: Flask를 사용하여 이미지 파일을 입력받아 분석 결과를 JSON 형태로 반환하는 API 서버를 구축, 모바일 앱이나 웹 서비스와 쉽게 연동할 수 있습니다.

📜 상세 정보 조회: 식별된 알약의 품목기준코드를 이용해 공공데이터포털 API를 호출하여 효능, 용법, 주의사항 등 상세 정보를 제공합니다.

🛠️ 기술 스택
AI / Machine Learning: TensorFlow/Keras, Ultralytics YOLOv8, Scikit-learn

OCR: Tesseract, Naver CLOVA OCR API

Image Processing: OpenCV, Pillow

Backend Framework: Flask, Flask-CORS

Dependencies: python-dotenv, requests, numpy

📂 프로젝트 구조
.
├── weights/
│   ├── detection_model.pt  # 알약 탐지 YOLO 모델
│   └── shape_model.h5      # 알약 모양 분류 Keras 모델
├── database/
│   └── pill.csv            # 알약 정보 데이터베이스
├── test_image/
│   └── sample.png          # 로컬 테스트용 샘플 이미지
├── output_images/          # 분석 결과 이미지가 저장되는 폴더
├── fonts/
│   └── malgun.ttf          # 결과 이미지에 한글 표기를 위한 폰트
│
├── main.py                 # 💻 로컬 이미지 분석 실행 스크립트
├── flask_server.py         # 🌐 웹 API 서버 실행 스크립트
│
├── object_detection.py     # YOLO 알약 탐지 모듈
├── image_preprocessing.py  # 이미지 배경 제거 및 전처리 모듈
├── shape_analysis.py       # 모양 분석 모듈
├── color_analysis.py       # 색상 분석 모듈
├── imprint_analysis.py     # 각인 분석(Tesseract) 모듈
├── database_handler.py     # DB 검색 및 매칭 모듈
├── api_handler.py          # 공공데이터포털 API 연동 모듈
│
├── .env                    # API 키 등 환경 변수 설정 파일
└── requirements.txt        # 프로젝트 의존성 라이브러리 목록
⚙️ 설치 및 환경 설정
Git 저장소 복제

Bash

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
필수 라이브러리 설치

Bash

pip install -r requirements.txt
(주의: requirements.txt 파일에 tensorflow, ultralytics, opencv-python, flask, python-dotenv, scikit-learn, requests, Pillow, pytesseract 등이 포함되어 있어야 합니다.)

Tesseract OCR 설치 (필수)

각인 분석을 위해 Tesseract OCR 엔진이 시스템에 설치되어 있어야 합니다.

Tesseract at UB Mannheim에서 자신의 OS에 맞는 설치 파일을 다운로드하여 설치하세요.

설치 후, imprint_analysis.py 파일 상단의 경로를 실제 Tesseract가 설치된 경로로 수정해야 할 수 있습니다.

Python

# imprint_analysis.py
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # 예시 경로
환경 변수 설정 (.env 파일)

프로젝트 루트 디렉터리에 .env 파일을 생성하고, 아래 내용을 채워 넣으세요.

공공데이터포털과 Naver Cloud Platform에서 API 키를 발급받아야 합니다.

코드 스니펫

# .env
GO_DATA_API_KEY="공공데이터포털에서 발급받은 Decoding 인증키"
NAVER_CLOVA_API_KEY="Naver CLOVA OCR Secret Key"
AI 모델 및 데이터 준비

학습된 AI 모델 가중치 파일(detection_model.pt, shape_model.h5)을 weights/ 폴더에 위치시킵니다.

알약 정보가 담긴 pill.csv 파일을 database/ 폴더에 위치시킵니다.

▶️ 실행 방법
이 프로젝트는 두 가지 방식으로 실행할 수 있습니다.

1. 로컬에서 단일 이미지 분석 (main.py)
로컬에 저장된 특정 이미지를 분석하고, 탐지 및 분석 결과가 담긴 이미지를 output_images/ 폴더에 저장합니다. 코드 테스트 및 디버깅에 유용합니다.

main.py 파일에서 분석할 이미지 경로를 수정합니다.

Python

# main.py
IMAGE_PATH = "test_image/sample.png"
아래 명령어로 스크립트를 실행합니다.

Bash

python main.py
콘솔에 분석 과정과 결과가 출력되며, output_images/ 폴더에 최종 결과 이미지가 저장됩니다.

2. 웹 API 서버 실행 (flask_server.py)
Flask를 이용해 API 서버를 실행합니다. 외부(예: 모바일 앱)에서 이미지 파일을 전송하면, 분석 결과를 JSON 형태로 반환합니다.

아래 명령어로 Flask 서버를 실행합니다.

Bash

python flask_server.py
서버가 http://0.0.0.0:5000 에서 실행되면, /predict 엔드포인트로 multipart/form-data 형식의 POST 요청을 보냅니다.

Key: file

Value: 분석할 이미지 파일

서버는 분석 결과(후보 알약 정보, 결과 이미지)를 JSON 형식으로 응답합니다.

📄 각 파일 기능 설명
파일명	주요 기능
main.py	로컬 실행 스크립트. 정해진 이미지 경로를 불러와 전체 분석 파이프라인을 실행하고 결과를 저장합니다.
flask_server.py	웹 API 서버. HTTP 요청으로 이미지를 받아 실시간으로 분석하고 결과를 JSON으로 반환합니다.
object_detection.py	객체 탐지 모듈. YOLOv8 모델을 사용하여 이미지 내의 모든 알약의 위치를 찾아냅니다.
image_preprocessing.py	이미지 전처리 모듈. GrabCut 알고리즘으로 알약 이미지의 배경을 정교하게 제거합니다.
shape_analysis.py	모양 분석 모듈. Keras 모델을 이용해 알약의 모양(원형, 타원형 등)을 분류하고 신뢰도를 반환합니다.
color_analysis.py	색상 분석 모듈. K-Means 클러스터링으로 알약의 주요 색상을 추출하고 가장 가까운 색상 후보를 찾습니다.
imprint_analysis.py	각인 분석 모듈 (Tesseract). 다양한 전처리 기법과 Tesseract OCR을 통해 알약 표면의 텍스트를 인식합니다.
imprint_analysis_naver.py	각인 분석 모듈 (Naver). Naver CLOVA OCR API를 사용하여 더 높은 정확도로 텍스트를 인식합니다. (선택적 사용)
database_handler.py	데이터베이스 핸들러. CSV DB를 로드하고, 분석된 특징들과 DB를 비교하여 가장 일치하는 알약을 찾습니다.
api_handler.py	외부 API 핸들러. 공공데이터포털 API를 호출하여 식별된 알약의 상세 정보를 조회합니다.
