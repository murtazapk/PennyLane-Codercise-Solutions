# PF.4.4 Codercise
import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires = 2)

@qml.qnode(dev, diff_method = "parameter-shift", max_diff = 2)
def circuit_for_hessian(params):
    """
    Implements the circuit shown in the codercise statement
    Args:
    - params (np.ndarray): [theta_0, theta_1, theta_2, theta_3]
    Returns:
    - np.tensor: <Z0xZ1>
    """

    ####################
    ###YOUR CODE HERE###
    ####################
    qml.RY(params[0], wires=0)
    qml.IsingXX(params[1], wires=[0, 1])
    qml.RX(params[2], wires=0)
    qml.RX(params[3], wires=1)

    return qml.expval(qml.PauliZ(0) @ qml.PauliZ(1)) # Return the expectation value required

test_params = np.array([0.1,0.2,0.3,0.4], requires_grad = True)
# Don't change test_params! 

hessian =qml.jacobian(qml.jacobian(circuit_for_hessian))(test_params) # Compute the Hessian
print("The hessian of the circuit is: \n", hessian)
