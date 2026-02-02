#codercise 1.1.1


import pennylane as qml
from pennylane import numpy as np
ket_0=np.array([1,0])
ket_1=np.array([0,1])
def normalize_state(alpha,beta):
    unnormalized_state=np.array([alpha,beta], dtype=np.complex128)
    norm=np.linalg.norm(unnormalized_state)
    normalized_state=unnormalized_state/norm

    return normalized_state
    pass

