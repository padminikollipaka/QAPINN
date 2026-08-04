# Quantum Assisted Physics Informed Neural Network (QAPINN)

## Objective

Solve Burgers' Equation using

- Classical PINN
- Quantum Neural Network
- Hybrid Quantum Assisted PINN

---

## Technologies

Python

PyTorch

PennyLane

NumPy

Matplotlib

---

## Folder Structure

src/

classical_pinn/

quantum_layer/

qapinn/

utils/

---

## Run Classical PINN

python -m src.classical_pinn.train

python -m src.classical_pinn.evaluate

---

## Plot Loss

python -m src.utils.plot_loss

---

## Test Quantum Layer

python test_quantum.py

---

## Train Hybrid QAPINN

python -m src.qapinn.train

---

## Evaluate Hybrid Model

python -m src.qapinn.evaluate

---

## Plot Hybrid Loss

python -m src.utils.plot_qapinn_loss