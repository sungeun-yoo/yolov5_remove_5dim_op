# yolov5_remove_5dim_op
Remove 5 dimension OP for NPU


# Install
> pip install -r requirement.txt

# Run
## Make or Moddifiy xxx_config.py

- Onnx path and result onnx path<br>
- 5dim Operator list-up <br>


```
onnx_path = '/usr/src/yolov5_remove_5dim_op/yolo_v5_s.onnx'
modi_onnx_path ='/usr/src/yolov5_remove_5dim_op/yolo_v5_s_4dim.onnx'
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
```

## Run script with config file
```
python 5dim_2_4dim.py
```
5 dim OP <br>
<img src = ".//resource/5dim_onnx.png" width="50%" height="50%">

4 dim OP <br>
<img src = ".//resource/4dim_onnx.png" width="50%" height="50%">

