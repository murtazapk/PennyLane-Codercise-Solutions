import pennylane as qml
import matplotlib.pyplot as plt
import numpy as np
from pennylane import numpy as np

# A.1.1
n=4
dev=qml.device("default.qubit",wires=n)
@qml.qnode(dev)

def hhcircuit():
    for i in range(n):
        qml.Hadamard(wires=i)

    return qml.probs(wires=range(n))
print(qml.draw(hhcircuit)())
