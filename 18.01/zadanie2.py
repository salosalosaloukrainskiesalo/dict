import numpy as np

A = np.array([[2, 1], [1,-3]])
B = np.array([8,1])

rozwianzanie = np.linalg.solve(A,B)

print(rozwianzanie)