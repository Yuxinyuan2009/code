import tensorcircuit as tc
import numpy as np

def pseudoinverse(A: np.ndarray) -> np.ndarray:
    """
    实现A的伪逆
    """
    print(A)
    u, s, Vh = np.linalg.svd(A)
    s_inv = np.zeros_like(A)
    print(A.shape[0])
    for i in range(A.shape[0]):
        print(s[i])
        if s[i] > 1e-10:
            s_inv[i, i] = 1.0 / s[i]
            print(s_inv[i, i])
    print(s_inv)
    A_inv = Vh.T @ s_inv @ u.T
    return A_inv
A = np.array([[1., 1., 2.], [1., 2., 1.], [1., 1., 1.]])
B = pseudoinverse(A)
print(B @ A)
v = np.arange(3)
print(B @ A @ v)