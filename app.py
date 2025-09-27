

# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import ImageFont
import cv2
import numpy as np
import base64
from tensorflow.keras.models import load_model

# 로컬 모듈 임포트
from object_detection import detect_pills
from database_handler import load_database
from api_handler import get_pill_details_from_api
from pill_analyzer import process_and_visualize_pills 

# --- Flask 앱 초기화 ---
app = Flask(__name__)
CORS(app)

# --- 전역 변수 및 모델/폰트 로딩 ---
YOLO_MODEL_PATH = "weights/detection_model.pt"
SHAPE_MODEL_PATH = "weights/shape_model.h5"
DB_PATH = "database/pill.csv"
FONT_PATH_BOLD = "fonts/malgunbd.ttf"
FONT_SIZE = 18

PILL_DB = load_database(DB_PATH)
SHAPE_MODEL = None
try:
    SHAPE_MODEL = load_model(SHAPE_MODEL_PATH)
    print(f"'{SHAPE_MODEL_PATH}' 모델 로딩 성공.")
except Exception as e:
    print(f"오류: '{SHAPE_MODEL_PATH}' 모델 로딩 실패. {e}")

PIL_FONT = ImageFont.load_default()
try:
    PIL_FONT = ImageFont.truetype(FONT_PATH_BOLD, FONT_SIZE)
except IOError:
    print(f"경고: '{FONT_PATH_BOLD}' 폰트 로딩 실패.")

# --- API 엔드포인트 ---
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': '파일이 없습니다.'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '파일이 선택되지 않았습니다.'}), 400

    # 1. 이미지 읽기
    filestr = file.read()
    npimg = np.frombuffer(filestr, np.uint8)
    original_image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # 2. 알약 탐지
    pill_boxes = detect_pills(original_image, YOLO_MODEL_PATH)
    
    # 3. 이미지 처리, 분석, 시각화를 단 한 줄의 함수 호출
    processed_image, candidates = process_and_visualize_pills(
        original_image, pill_boxes, SHAPE_MODEL, PILL_DB, PIL_FONT
    )
    
    # 4. 결과를 Base64로 인코딩하여 JSON으로 반환
    _, buffer = cv2.imencode('.jpg', processed_image)
    img_str = base64.b64encode(buffer).decode('utf-8')
    
    return jsonify({
        'image': 'data:image/jpeg;base64,' + img_str,
        'candidates': candidates
    })

@app.route('/detail')
def detail():
    item_code = request.args.get('code')
    if not item_code:
        return jsonify({'error': '품목기준코드가 필요합니다.'}), 400
        
    details = get_pill_details_from_api(item_code)
    return jsonify(details)

# --- 서버 실행 ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)