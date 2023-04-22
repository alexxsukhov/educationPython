# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# Сделал через строку, объясняю почему, билет может быть с номером 023005, что числом не является, а набором цифр

num_ticket = input("Введите номер билета для проверки: ")
length = len(num_ticket)

if length == 6:
    summ_left = 0
    summ_right = 0

    half_len = length // 2

    i = 0
    for item in num_ticket:
        if i < half_len:
            summ_left = summ_left + int(item)
        if half_len <= i <= length - 1:
            summ_right = summ_right + int(item)
        i = i + 1

    if summ_right == summ_left:
        print("Билет счастливый")
    else:
        print("Билет несчастливый")
else:
    print("Введите корректный номер")