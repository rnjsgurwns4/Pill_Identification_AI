네, GitHub `README.md` 파일에서 `#` 기호는 **마크다운(Markdown)** 문법에서 \*\*제목(Heading)\*\*을 나타내는 데 사용됩니다.

  * `#` (하나)는 가장 큰 제목(H1)을 의미합니다. (`<h1>`)
  * `##` (두 개)는 그 다음 큰 제목(H2)을 의미합니다. (`<h2>`)
  * `###` (세 개)는 그 다음 제목(H3)을 의미합니다. (`<h3>`)
  * 최대 `######` (여섯 개)까지 사용할 수 있습니다.

제목은 문서의 구조를 나누고 내용을 체계적으로 보여주는 중요한 역할을 합니다.

-----

제공해주신 내용과 기존 `README.md` 형식을 조합하여 새롭게 구성했습니다. 팀 페이지, 발표 자료 링크 및 프로젝트 소개, 소개 영상, 팀 소개 섹션이 추가되었습니다.

아래 내용을 복사하여 GitHub 프로젝트의 `README.md` 파일에 붙여넣으세요.

-----

# 💊 AI 알약 식별 프로젝트 (AI Pill Identifier)

[](https://www.google.com/search?q=https://github.com/your-username/your-repository-name)
[](https://www.python.org)
[](https://www.tensorflow.org/)
[](https://www.google.com/search?q=https://ultralytics.com/)
[](https://flask.palletsprojects.com/)
[](https://opensource.org/licenses/MIT)

이미지 한 장으로 알약의 모양, 색상, 각인(글자)을 종합적으로 분석하여 어떤 약인지 식별해주는 AI 기반 시스템입니다.

<br>

**팀 페이지 주소**: [https://kookmin-sw.github.io/capstone-2021-22](https://kookmin-sw.github.io/capstone-2021-22)
**중간발표 주소**: [https://drive.google.com/file/d/1kPHVM13y5LI24Fdjgq\_JBC69lQjyPFsl/view?usp=sharing](https://drive.google.com/file/d/1kPHVM13y5LI24Fdjgq_JBC69lQjyPFsl/view?usp=sharing)
**최종발표 주소**: [https://youtu.be/-fjrBTSwmu4](https://youtu.be/-fjrBTSwmu4)

<br>

## 📚 목차 (Table of Contents)

1.  [프로젝트 소개](https://www.google.com/search?q=%231-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%86%8C%EA%B0%9C)
      * [주요 기능](https://www.google.com/search?q=%23%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5)
      * [프로젝트 구성도](https://www.google.com/search?q=%23%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B5%AC%EC%84%B1%EB%8F%84)
      * [기대 효과](https://www.google.com/search?q=%23%EA%B8%B0%EB%8C%80%ED%9A%A8%EA%B3%BC)
2.  [소개 영상](https://www.google.com/search?q=%232-%EC%86%8C%EA%B0%9C-%EC%98%81%EC%83%81)
3.  [팀 소개](https://www.google.com/search?q=%233-%ED%8C%80-%EC%86%8C%EA%B0%9C)
4.  [주요 기능 (시스템)](https://www.google.com/search?q=%23-%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%8B%9C%EC%8A%A4%ED%85%9C)
5.  [기술 스택](https://www.google.com/search?q=%23-%EA%B8%B0%EC%88%A0-%EC%8A%A4%ED%83%9D)
6.  [프로젝트 구조](https://www.google.com/search?q=%23-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B5%AC%EC%A1%B0)
7.  [설치 및 환경 설정](https://www.google.com/search?q=%23%EF%B8%8F-%EC%84%A4%EC%B9%98-%EB%B0%8F-%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95)
8.  [실행 방법](https://www.google.com/search?q=%23%EF%B8%8F-%EC%8B%A4%ED%96%89-%EB%B0%A9%EB%B2%95)
9.  [각 파일 기능 설명](https://www.google.com/search?q=%23-%EA%B0%81-%ED%8C%8C%EC%9D%BC-%EA%B8%B0%EB%8A%A5-%EC%84%A4%EB%AA%85)
10. [기여 방법](https://www.google.com/search?q=%23-%EA%B8%B0%EC%97%AC-%EB%B0%A9%EB%B2%95)
11. [라이선스](https://www.google.com/search?q=%23-%EB%9D%BC%EC%9D%B4%EC%84%A0%EC%8A%A4)

<br>

-----

## 1\. 프로젝트 소개

\<img src="[https://user-images.githubusercontent.com/28584133/118848501-c40d9200-b909-11eb-86b1-a460692ac6fa.png](https://user-images.githubusercontent.com/28584133/118848501-c40d9200-b909-11eb-86b1-a460692ac6fa.png)" alt="logo" width="50%"\>
현대 의학이 발전하면서 시중의 의약품의 종류도 많아졌습니다.
각 의약품마다 용도와 용법이 존재하지만, 복용하는 약의 종류가 많아질수록 자신이 무슨 약을 복용하는지 헷갈리는 경우가 생깁니다.
또한 약국에서 구입한 알약의 패키지나 처방받은 약의 봉투를 잃어버렸을 경우, 해당 알약이 어떤 알약인지 쉽게 알지 못합니다.
이러한 문제점을 해결하기 위해 우리는 사진 촬영만으로 알약 검색이 가능한 이미지 기반 알약 식별 모바일 애플리케이션 개발을 목표로 합니다.

### 주요 기능

1.  **알약 검색**
      * 알약 사진 촬영을 통한 검색
      * 텍스트 정보(이름, 효능 등)를 통한 검색
2.  **내 약통 기능**
      * 사용자가 복용하고 있는 약의 종류를 관리할 수 있는 즐겨찾기 기능

### 프로젝트 구성도

### 기대효과

'이게뭐약?' 개발을 통해 일상생활에서 누구나 의약품을 쉽고 빠르게 식별 가능하도록 하여 의약품 정보 활용의 기회를 넓힙니다. 또한 얻은 의약품의 정보를 통해 비슷한 약의 중복 처방으로 인한 오남용, 잘못된 알약 복용 등의 문제를 미리 방지하여 사용자의 안전하고 건강한 의약품 소비를 기대해 볼 수 있습니다.

-----

## 2\. 소개 영상

### 홍보영상 보러가기

[](https://www.google.com/search?q=%5Bhttps://drive.google.com/file/d/1Zw7w_8N1e5AV6rv_GLk4jOZbXOUsoFyR/view%3Fusp%3Dsharing%5D\(https://drive.google.com/file/d/1Zw7w_8N1e5AV6rv_GLk4jOZbXOUsoFyR/view%3Fusp%3Dsharing\))

### 시연영상 보러가기

[](https://drive.google.com/file/d/1uk1CV_iIfjNnzZ5MIiyrygWHF8sZ8Njg/view?usp=sharing)

### 시연영상2 보러가기

[https://youtu.be/Yh6jDoGDLxA](https://youtu.be/Yh6jDoGDLxA)

-----

## 3\. 팀 소개

#### 김윤정

\<img src="[https://user-images.githubusercontent.com/28584226/113485108-f80e2e80-94e6-11eb-903b-1b324d57382f.jpeg](https://user-images.githubusercontent.com/28584226/113485108-f80e2e80-94e6-11eb-903b-1b324d57382f.jpeg)" alt="image-yunjeong" width= 30%/\>

```
Student ID: 20171600
E-mail: jje0ng@kookmin.ac.kr
Role: 팀장, AI 모델 개발, 데이터 라벨링
```

#### 고지원

\<img src="[https://user-images.githubusercontent.com/28584226/113485623-82579200-94e9-11eb-8fbb-02e12f73396c.jpeg](https://user-images.githubusercontent.com/28584226/113485623-82579200-94e9-11eb-8fbb-02e12f73396c.jpeg)" alt="image-jiwon" width= 30% /\>

```
Student ID: 20171577
E-mail: gggoe@kookmin.ac.kr
Role: UI/UX 디자인 및 앱 기획, 클라이언트 개발
```

-----

## ✨ 주요 기능 (시스템)

  * **🧠 다중 객체 탐지**: 한 이미지에 여러 개의 알약이 있어도 **YOLOv8** 모델이 각각의 위치를 정확하게 탐지합니다.
  * **🎨 정교한 특징 추출**:
      * **모양**: 직접 학습시킨 **TensorFlow/Keras** 모델을 통해 원형, 타원형 등 알약의 형태를 분류합니다.
      * **색상**: **K-Means 클러스터링** 알고리즘으로 배경이 제거된 이미지에서 가장 지배적인 색상을 추출합니다.
      * **각인**: **Tesseract OCR** 및 **Naver CLOVA OCR**을 활용, 다양한 전처리 기법을 적용하여 알약 표면의 글자나 숫자를 인식합니다.
  * **🔍 데이터베이스 매칭**: 추출된 특징(모양, 색상, 각인)을 종합하여 데이터베이스와 비교하고, 가장 유사한 알약 후보를 점수와 함께 제시합니다.
  * **🌐 웹 API 제공**: **Flask**를 사용하여 이미지 파일을 입력받아 분석 결과를 JSON 형태로 반환하는 API 서버를 구축, 모바일 앱이나 웹 서비스와 쉽게 연동할 수 있습니다.
  * **📜 상세 정보 조회**: 식별된 알약의 품목기준코드를 이용해 공공데이터포털 API를 호출하여 효능, 용법, 주의사항 등 상세 정보를 제공합니다.

-----

## 🛠️ 기술 스택

  * **AI / Machine Learning**: TensorFlow/Keras, Ultralytics YOLOv8, Scikit-learn
  * **OCR**: Tesseract, Naver CLOVA OCR API
  * **Image Processing**: OpenCV, Pillow
  * **Backend Framework**: Flask, Flask-CORS
  * **Dependencies**: `python-dotenv`, `requests`, `numpy`

-----

## 📂 프로젝트 구조

```
.
├── weights/              # AI 모델 가중치 파일 (.pt, .h5)
├── database/             # 알약 DB (pill.csv)
├── test_image/           # 로컬 테스트용 이미지
├── output_images/        # 분석 결과 이미지가 저장되는 폴더
├── fonts/                # 한글 폰트 파일 (.ttf)
│
├── main.py               # 💻 로컬 이미지 분석 실행 스크립트
├── flask_server.py       # 🌐 웹 API 서버 실행 스크립트
│
├── object_detection.py   # ... (각 기능별 분석 모듈)
├── shape_analysis.py
├── ...
│
├── .env                  # API 키 등 환경 변수 설정 파일
└── requirements.txt      # 프로젝트 의존성 라이브러리 목록
```

-----

## ⚙️ 설치 및 환경 설정

### 1\. Git 저장소 복제

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2\. 가상 환경 생성 및 활성화 (권장)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3\. 필수 라이브러리 설치

```bash
pip install -r requirements.txt
```

> **Note**: `requirements.txt` 파일에 `tensorflow`, `ultralytics`, `opencv-python`, `flask`, `python-dotenv`, `scikit-learn`, `requests`, `Pillow`, `pytesseract` 등이 포함되어 있어야 합니다.

### 4\. Tesseract OCR 설치 (필수)

각인 분석을 위해 Tesseract OCR 엔진이 시스템에 설치되어 있어야 합니다.

  - **설치**: [Tesseract at UB Mannheim](https://www.google.com/search?q=https://github.com/UB-Mannheim/tesseract/wiki)에서 자신의 OS에 맞는 설치 파일을 다운로드하여 설치하세요.
  - **경로 설정**: 설치 후, `imprint_analysis.py` 파일 상단의 경로를 실제 Tesseract가 설치된 경로로 수정해야 할 수 있습니다.
    ```python
    # imprint_analysis.py
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # 예시 경로
    ```

### 5\. 환경 변수 설정 (`.env` 파일)

프로젝트 루트 디렉터리에 `.env` 파일을 생성하고, 아래 형식에 맞춰 API 키를 입력하세요.

```env
# .env.example - 이 내용을 .env 파일에 복사하여 사용하세요.
GO_DATA_API_KEY="공공데이터포털에서 발급받은 Decoding 인증키"
NAVER_CLOVA_API_KEY="Naver CLOVA OCR Secret Key"
```

### 6\. AI 모델 및 데이터 준비

  - 학습된 AI 모델 가중치 파일(`detection_model.pt`, `shape_model.h5`)을 `weights/` 폴더에 위치시킵니다.
  - 알약 정보가 담긴 `pill.csv` 파일을 `database/` 폴더에 위치시킵니다.

-----

## ▶️ 실행 방법

### 💻 로컬에서 단일 이미지 분석 (`main.py`)

로컬 이미지를 직접 분석하고 결과를 `output_images/` 폴더에 저장합니다. 코드 테스트 및 디버깅에 유용합니다.

1.  `main.py` 파일에서 분석할 이미지 경로를 수정합니다.
    ```python
    IMAGE_PATH = "test_image/sample.png"
    ```
2.  아래 명령어로 스크립트를 실행합니다.
    ```bash
    python main.py
    ```

### 🌐 웹 API 서버 실행 (`flask_server.py`)

Flask 기반의 API 서버를 실행하여 외부 요청을 받아 실시간으로 분석 결과를 반환합니다.

1.  아래 명령어로 Flask 서버를 실행합니다.
    ```bash
    python flask_server.py
    ```
2.  서버가 `http://0.0.0.0:5000` 에서 실행되면, `/predict` 엔드포인트로 이미지 파일을 `multipart/form-data` 형식의 POST 요청을 보냅니다. (Key: `file`)

-----

## 📄 각 파일 기능 설명

| 파일명                     | 주요 기능                                                                                             |
| :------------------------- | :---------------------------------------------------------------------------------------------------- |
| `main.py`                  | **로컬 실행 스크립트**. 정해진 이미지 경로를 불러와 전체 분석 파이프라인을 실행하고 결과를 저장합니다.     |
| `flask_server.py`          | **웹 API 서버**. HTTP 요청으로 이미지를 받아 실시간으로 분석하고 결과를 JSON으로 반환합니다.               |
| `object_detection.py`      | **객체 탐지 모듈**. YOLOv8 모델을 사용하여 이미지 내의 모든 알약의 위치를 찾아냅니다.                     |
| `image_preprocessing.py`   | **이미지 전처리 모듈**. GrabCut 알고리즘으로 알약 이미지의 배경을 정교하게 제거합니다.                      |
| `shape_analysis.py`        | **모양 분석 모듈**. Keras 모델을 이용해 알약의 모양(원형, 타원형 등)을 분류합니다.                     |
| `color_analysis.py`        | **색상 분석 모듈**. K-Means 클러스터링으로 알약의 주요 색상을 추출합니다.                                   |
| `imprint_analysis.py`      | **각인 분석 모듈**. Tesseract OCR과 다양한 전처리 기법으로 알약 표면의 텍스트를 인식합니다.                   |
| `imprint_analysis_naver.py`| **각인 분석 모듈 (Naver)**. Naver CLOVA OCR API를 사용하여 텍스트를 인식합니다. (선택적 사용)                 |
| `database_handler.py`      | **데이터베이스 핸들러**. 분석된 특징들과 DB를 비교하여 가장 일치하는 알약을 찾습니다.                  |
| `api_handler.py`           | **외부 API 핸들러**. 공공데이터포털 API를 호출하여 식별된 알약의 상세 정보를 조회합니다.                  |

-----

## 🙌 기여 방법 (Contributing)

이 프로젝트에 기여하고 싶으시다면 언제든지 환영합니다\!

1.  이 저장소를 Fork 하세요.
2.  새로운 기능 브랜치를 생성하세요 (`git checkout -b feature/AmazingFeature`).
3.  변경 사항을 커밋하세요 (`git commit -m 'Add some AmazingFeature'`).
4.  브랜치에 Push 하세요 (`git push origin feature/AmazingFeature`).
5.  Pull Request를 열어주세요.

-----

## 📜 라이선스 (License)

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 `LICENSE` 파일을 참고하세요.

-----
