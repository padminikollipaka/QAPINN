import torch

from src.quantum_layer.quantum_layer import QuantumLayer

layer = QuantumLayer()

x = torch.tensor([[0.5, 0.2]], dtype=torch.float32)

output = layer(x)

print("Quantum Output:")
print(output)

print("Shape:")
print(output.shape)