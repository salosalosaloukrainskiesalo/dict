import numpy as np 
import pandas as pb


np.random.seed(42)


rozmiar_tablicy = 5
data = np.random.rand(rozmiar_tablicy, 3)
macierz = pb.DataFrame(data, columns=['Column1', 'Column2', 'Column3'])

print(macierz,"\n")

srednie = macierz.mean()
mediany = macierz.median()
odchylenia_standardowe = macierz.std()

print("srednia\n", srednie)
print("mediana\n", mediany)
print("odhylenia standardowe\n", odchylenia_standardowe)