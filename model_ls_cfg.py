
onnx_path = '/usr/src/yolov5_remove_5dim_op/yolov5ls_hphf231017_relu.onnx'
modi_onnx_path ='/usr/src/yolov5_remove_5dim_op/yolov5ls_hphf231017_relu_4dim.onnx'
json_path =''

reshape_name_list = [
    "onnx::Reshape_584",
    "onnx::Reshape_594",
    "onnx::Reshape_604"
]

traspose_name_list = [
    'Transpose_248',
    'Transpose_267',
    'Transpose_286'
]

split_name_list = [
    'Split_250',
    'Split_269',
    'Split_288'
]

anchor_process_name_list = [
    'onnx::Add_482',
    'onnx::Mul_490',

    'onnx::Add_520',
    'onnx::Mul_528',

    'onnx::Add_558',
    'onnx::Mul_566',
]

concat_name_list = [
    'Concat_263',
    'Concat_282',
    'Concat_301'
]