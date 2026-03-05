import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code help
    x=np.array(x)
    return 1/(1+np.exp(-x))
    pass