# Codercise PF.1.1a Circuits as a Functions
import pennylane as qml
from pennylane import numpy as np


dev = qml.device("default.qubit", wires=3)

@qml.qnode(dev)
def circuit_as_function(params):
    theta_0, theta_1, theta_2, theta_3 = params

    # First rotation
    qml.RX(theta_0, wires=0)

    # Entangling gates
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.CNOT(wires=[2, 0])

    # Final rotations
    qml.RY(theta_1, wires=0)
    qml.RY(theta_2, wires=1)
    qml.RY(theta_3, wires=2)

    return qml.expval(qml.PauliZ(0))


angles = np.linspace(0, 4 * np.pi, 200)
output_values = np.array([circuit_as_function([0.5, t, 0.5, 0.5]) for t in angles])

