
onnx_path = '/usr/src/yolov5_remove_5dim_op/yolo_v5_s_creatz.onnx'
modi_onnx_path ='/usr/src/yolov5_remove_5dim_op/yolo_v5_s_creatz_4dim.onnx'
json_path =''

reshape_name_list = [
    "onnx::Reshape_394",
    "onnx::Reshape_404",
    "onnx::Reshape_414"
]

split_name_list = [
    'Split_148',
    'Split_167',
    'Split_186'
]

traspose_name_list = [
    'Transpose_146',
    'Transpose_165',
    'Transpose_184'
]

anchor_process_name_list = [
    'onnx::Add_292',
    'onnx::Mul_300',

    'onnx::Add_330',
    'onnx::Mul_338',

    'onnx::Add_368',
    'onnx::Mul_376',
]

concat_name_list = [
    'Concat_161',
    'Concat_180',
    'Concat_199'
]