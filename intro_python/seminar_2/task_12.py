s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

for i in range(s):
    for j in range(p):
        if j + i == s and j * i == p:
            print(f"Первое число: {i}\nВторое число: {j}")