n = int(input("Введите общее количество монет: "))
count_head = 0
count_tail = 0

for item in range(n):
    head_tail = int(input("Какой стороной лежит монета 0 = орел, 1 = решка: "))
    if head_tail == 1:
        count_tail = count_tail + 1
    else:
        count_head = count_head + 1

if count_head < count_tail:
    print(f"Необходимо перевернуть орлов в количестве: {count_head}")
elif count_head > count_tail:
    print(f"Необходимо перевернуть решек в количестве: {count_tail}")
else:
    print(f"Монеток равное количество!")