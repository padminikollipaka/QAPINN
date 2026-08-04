import torch

from src.qapinn.model import QAPINN

model = QAPINN()

x = torch.tensor([[0.5, 0.2]], dtype=torch.float32)

output = model(x)

print("QAPINN Output:")
print(output)

print("Output Shape:")
print(output.shape)