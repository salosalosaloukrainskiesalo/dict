import numpy as np

def suma_diagonali (arr) :
    diagonal_elements = np.diagonal(arr)
    sumdiag = np.sum(diagonal_elements)
    return sumdiag

a = np.array ([[1 , 2 , 3], [4 , 5 , 6], [7 , 8 , 9]])
i = suma_diagonali (a)
print (x)
