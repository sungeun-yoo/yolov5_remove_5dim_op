import os
import argparse
from onnx2json import convert
from json2onnx import convert as convertor_json2onnx
import base64
import struct

from sed4onnx import encode
from sed4onnx import decode

# Argument parser setup
parser = argparse.ArgumentParser(description='Select model configuration.')
parser.add_argument('--model-config', choices=['s', 'm', 'ls'], help='Model configuration: s, m, or ls')
args = parser.parse_args()

# Conditional import based on the argument
if args.model_config == 's':
    from model_s_cfg import *
elif args.model_config == 'm':
    from model_m_cfg import *
elif args.model_config == 'ls':
    from model_ls_cfg import *

onnx_json = convert(
  input_onnx_file_path=onnx_path,
  output_json_path=json_path,
  json_indent=2,
)

# 재귀적으로 검색
def find_in_dict(obj, key, value):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key and v == value:
                return obj
            found = find_in_dict(v, key, value)
            if found:
                return found
    elif isinstance(obj, list):
        for item in obj:
            found = find_in_dict(item, key, value)
            if found:
                return found
    return None

# Split
for name in split_name_list:
    print("name : ",name)
    result = find_in_dict(onnx_json, "name", name)
    print(result)
    for attr in result['attribute']:
        if attr['name'] == 'axis':
            attr['i'] = '3'
    print(result)

# Transpose
for name in traspose_name_list:
    result = find_in_dict(onnx_json, "name", name)
    print(result)
    for attr in result['attribute']:
        if attr['name'] == 'perm':
            attr['ints'] = ['0','2','3','1']
    print(result)

# Reshape Dim 5 to 4
for name in reshape_name_list:
    result = find_in_dict(onnx_json, "name", name)
    if result:
        print(result)
    else:
        print("Not found.")

    # rawData를 Base64로부터 디코딩
    decoded_bytes = base64.b64decode(result['rawData'])
    # 디코딩된 바이트를 int64 배열로 변환
    int64_values = [struct.unpack('q', decoded_bytes[i:i+8])[0] for i in range(0, len(decoded_bytes), 8)]
    print(int64_values)

    # int64_values의 길이가 5인지 확인
    if len(int64_values) == 5:
        # 첫 번째 요소 제거
        int64_values.pop(0)
    else:
        print("The list does not contain 5 elements.")

    print(str(int64_values))

    base64_string = encode(
    constant_string=str(int64_values),
    dtype='int64',
    )

    print("rawDatastring : ", result['rawData'])
    print("base64_string : ", base64_string)

    result['rawData'] = base64_string
    result['dims'] = ['4']
    print(result)
    print('-------------------------------------------')


for name in anchor_process_name_list:
    result = find_in_dict(onnx_json, "name", name)
    print(result['dims'])
    result['dims'].pop(0)
    print(result['dims'])


for name in concat_name_list:
    result = find_in_dict(onnx_json, "name", name)
    print(result)
    for attr in result['attribute']:
        if attr['name'] == 'axis':
            attr['i'] = '3'
    print(result)

onnx_graph = convertor_json2onnx(
  json_dict=onnx_json,
  output_onnx_file_path=modi_onnx_path,
)