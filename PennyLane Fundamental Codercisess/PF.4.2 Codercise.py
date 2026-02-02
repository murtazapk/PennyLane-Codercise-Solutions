# PF.4.2 Codercise
import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires = 4)

@qml.qnode(dev)
def strong_entangler(weights):
    """
    Applies Strongly Entangling Layers to the default initial state
    Args:
    - weights (np.ndarray): The weights argument for qml.StronglyEntanglingLayers
    Returns:
    - (np.tensor): <Z0>
    """

    ####################
    ###YOUR CODE HERE###
    ####################
    qml.StronglyEntanglingLayers(weights, wires=range(4))
    
    return qml.expval(qml.PauliZ(0))

num_layers = 2
num_wires = 4
test_weights = np.random.random(size=(num_layers, num_wires, 3))

print("The output of your circuit with these weights is: ", strong_entangler(test_weights))
