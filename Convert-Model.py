from torch.autograd import Variable
import torch.onnx
import torch

import onnx
import onnx_caffe2.backend as backend
import numpy as np

# load model
model = torch.load("model.p")
model.cpu()

# Evaluation Mode
model.train(False)

# Create dummy input
dummy_input = Variable(torch.randn(1, 3, 224, 224))
output_torch = model(dummy_input)

# Export ONNX model
torch.onnx.export(model, dummy_input, "model.proto", verbose=True)

# Load ONNX model
graph = onnx.load("model.proto")

# Check Formation
onnx.checker.check_graph(graph)

# Print Graph to get blob names
onnx.helper.printable_graph(graph)

# Check model output
rep = backend.prepare(graph, device="CPU")
output_onnx = rep.run(dummy_input.cpu().data.numpy().astype(np.float32))

# Verify the numerical correctness upto 3 decimal places
np.testing.assert_almost_equal(output_torch.data.cpu().numpy(), output_onnx[0], decimal=3)