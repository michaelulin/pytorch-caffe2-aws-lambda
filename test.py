import ctypes
import os

for d, dirs, files in os.walk(os.path.join(os.getcwd(), 'local', 'lib')):
    for f in files:
        if f.endswith('.a'):
            continue
        ctypes.cdll.LoadLibrary(os.path.join(d, f))

import numpy as np
from caffe2.python import workspace
import json

def handler(event, context):
    x = np.random.rand(4, 3, 2)
    print(x)
    print(x.shape)

    workspace.FeedBlob("my_x", x)

    x2 = workspace.FetchBlob("my_x")
    ret = json.dumps(str(x2))

    return {"statusCode": 200, \
            "headers": {"Content-Type": "application/json"}, \
             "body": ret}

