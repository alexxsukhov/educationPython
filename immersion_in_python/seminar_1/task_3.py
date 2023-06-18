"""
3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

usr_number = int(input("Введите число от 1 до 10 000: "))

while usr_number > 10000 or usr_number < 1:
    print("Вы ввели некорретное значение")
    usr_number = int(input("Введите число от 1 до 10 000: "))

count_divider = 0

start_range = 2

for i in range(start_range, usr_number // 2):
    if usr_number % i == 0:
        count_divider += 1

if count_divider >= 2:
    print(f"Число {usr_number} не является простым")
else:
    print(f"Число {usr_number} является простым")
