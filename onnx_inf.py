import cv2
import numpy as np
import onnxruntime

img_path = '/usr/src/yolov5_remove_5dim_op/images/zidane.jpg'
model_path = 'last.onnx'

# 이미지 로드 및 리사이징
img = cv2.imread()
img = cv2.resize(img, (640, 480))

# 이미지 전처리: RGB 변환 및 정규화
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img.astype(np.float32) / 255.0
img = np.transpose(img, (2, 0, 1))
img = np.expand_dims(img, 0)  # 배치 차원 추가

# ONNX 모델 로드
ort_session = onnxruntime.InferenceSession(model_path)

# 입력 이름과 출력 이름 가져오기
input_name = ort_session.get_inputs()[0].name

# 'y' 노드의 이름을 명시적으로 지정하여 추론 실행
output_name = 'output' # 'y'라는 이름의 노드를 식별해야 합니다. 여기서 'y'는 예시입니다.
results = ort_session.run([output_name], {input_name: img})

# 결과 출력
print(results)
