import torch
from src.classical_pinn.model import PINN

# Create the model
model = PINN()

# Create sample input (x, t)
x = torch.tensor([[0.5, 0.2]], dtype=torch.float32)

# Get prediction
output = model(x)

print("Model Output:")
print(output)