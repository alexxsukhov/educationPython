a = int(input("Введите первое число: "))
n = int(input("Введите число: "))
d = int(input("Введите разницу прогрессии: "))

for i in range(n):
    an = a + i * d
    print(an, end=" ")
