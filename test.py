import boto3
import os

# Check if models are available

if os.path.isfile('/tmp/model.proto') != True:
    s3 = boto3.client('s3')
    s3.download_file('mybucket', 'model.proto', '/tmp/model.proto')


# Add libraries

import ctypes
import os

for d, dirs, files in os.walk(os.path.join(os.getcwd(), 'local', 'lib')):
    for f in files:
        if f.endswith('.a'):
            continue
        ctypes.cdll.LoadLibrary(os.path.join(d, f))

import numpy as np

import json
import onnx
import onnx_caffe2.backend as backend

# Load ONNX model
graph = onnx.load("/tmp/model.proto")

# Load model into Caffe2
model = backend.prepare(graph, device="CPU")


def handler(event, context):
    # Create dummy input for model
    x = np.random.randn(1, 3, 224, 224)

    # Get model output
    output = model.run(x.astype(np.float32))

    # return results formatted for AWS API Gateway
    return {"statusCode": 200, \
            "headers": {"Content-Type": "application/json"}, \
             "body": json.dumps(str(output))}

