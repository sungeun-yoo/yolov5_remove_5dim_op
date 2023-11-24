import onnx
from onnx import checker

# ONNX 모델 로드
model = onnx.load('yolov5m_512x256_creatz_mod.onnx')

# 모델 체크
checker.check_model(model)

# 그래프 체크
checker.check_graph(model.graph)

# 노드 체크 (모든 노드에 대해)
for node in model.graph.node:
    checker.check_node(node)
