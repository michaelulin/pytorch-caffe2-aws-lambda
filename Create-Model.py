import torch
from torchvision import models

model = models.resnet18(pretrained=True)
torch.save(model,"model.p")