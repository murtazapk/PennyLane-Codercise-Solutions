# A.2.1 Codercise: Matrix of the Oracle
import pennylane as qml
import matplotlib.pyplot as plt
import numpy as np
from pennylane import numpy as np

def oracle(combo):
    index=np.ravel_multi_index(combo, [2]*len(combo))
    my_array=np.identity(2**len(combo))
    my_array[index, index]=-1

    return my_array
