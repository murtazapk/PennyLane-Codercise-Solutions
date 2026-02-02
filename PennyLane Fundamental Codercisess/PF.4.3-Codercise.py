# PF.4.3 Codercise: How to Train your Qnode
import pennylane as qml
from pennylane import numpy as np
dev = qml.device("default.qubit", wires = 3)

@qml.qnode(dev)
def embedding_and_circuit(features, params):
    """
    A QNode that depends on trainable and non-trainable parameters
    Args:
    - features (np.ndarray): Non-trainable parameters in the AngleEmbedding routine
    - params (np.ndarray): Trainable parameters for the rest of the circuit
    Returns:
    - (np.tensor): <Z0>
    """

    ####################
    ###YOUR CODE HERE###
    ####################
    qml.AngleEmbedding(features, wires=[0,1,2])
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.CNOT(wires=[2, 0])
    qml.RY(params[0], wires=0)
    qml.RY(params[1], wires=1)
    qml.RY(params[2], wires=2)
    
    return qml.expval(qml.PauliZ(0))

features = np.array([0.3,0.4,0.6], requires_grad = False)
params = np.array([0.4,0.7,0.9], requires_grad = True)
print("The gradient of the circuit is:", qml.jacobian(embedding_and_circuit)(features, params))
