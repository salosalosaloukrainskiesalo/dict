a = []
print("podaj ilosc elementow listy")
size = int(input())
for i in range(0,size):
    b=int(input())
    a.append(b)

sumlist = sum(a)

print(sumlist)