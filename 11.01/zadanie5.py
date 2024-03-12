print("Podaj ilosc liczb w zbiorze:")
size = int(input())
zbior = set()

for i in range(size):
    n = int(input())
    zbior.add(n)

sumlist = sum(zbior)

print(sumlist)
