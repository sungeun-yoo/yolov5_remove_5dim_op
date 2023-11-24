import onnx
from onnx import checker

# ONNX 모델 로드
model = onnx.load('yolov5m_512x256_mod.onnx')

# 모델의 opset version을 11로 설정
model.opset_import[0].version = 11
# 모델 체크
print(checker.check_model(model))

# 그래프 체크
#checker.check_graph(model.graph)


# 노드 체크 (모든 노드에 대해)
#for node in model.graph.node:
#    checker.check_node(node)



import onnxsim
model_onnx, check = onnxsim.simplify(model)
assert check, 'assert check failed'
onnx.save(model_onnx, "yolov5m_512x256_mod_sim.onnx")