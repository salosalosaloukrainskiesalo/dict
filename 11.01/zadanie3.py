slownik = {'imie': 'piotr', 'wiek': 124, 'kraj': 'polska'}
print(slownik) 
print("jaki klucz chcesz usunac: ")
staryklucz = str(input())
print("jaki klucz chcesz dodac")
nowylycz = str(input())

if staryklucz == "imie":
    slownik[nowylycz]=slownik.pop(staryklucz)
elif staryklucz == "wiek":
    slownik[nowylycz]=slownik.pop(staryklucz)
elif staryklucz == 'kraj':
    slownik[nowylycz]=slownik.pop(staryklucz)

print("podaj nowa wartosc")
d=str(input())

slownik[nowylycz] = d 

print(slownik)