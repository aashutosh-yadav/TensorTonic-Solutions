import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    z = np.asarray(x,dtype=float)
    sigma = 1/(1+np.exp(-z))
    return sigma