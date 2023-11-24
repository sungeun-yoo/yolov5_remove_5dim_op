
onnx_path = '/usr/src/yolov5_remove_5dim_op/yolov5m_hphf231017_relu.onnx'
modi_onnx_path ='/usr/src/yolov5_remove_5dim_op/yolov5m_hphf231017_relu_4dim.onnx'
json_path =''

reshape_name_list = [
    "onnx::Reshape_489",
    "onnx::Reshape_499",
    "onnx::Reshape_509"
]

traspose_name_list = [
    'Transpose_197',
    'Transpose_216',
    'Transpose_235'
]

split_name_list = [
    'Split_199',
    'Split_218',
    'Split_237'
]

anchor_process_name_list = [
    'onnx::Add_387',
    'onnx::Mul_395',

    'onnx::Add_425',
    'onnx::Mul_433',

    'onnx::Add_463',
    'onnx::Mul_471',
]

concat_name_list = [
    'Concat_212',
    'Concat_231',
    'Concat_250'
]