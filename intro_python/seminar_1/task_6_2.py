number_ticket = input("Введите 6-значный номер билета: ")
length = len(number_ticket)

if length == 6:
    summ_left = int(number_ticket[0]) + int(number_ticket[1]) + int(number_ticket[3])
    summ_right = int(number_ticket[0]) + int(number_ticket[2]) + int(number_ticket[0])

    if summ_left == summ_right:
        print("Билетик счастливый")
    else:
        print("Билетик вполне обычный")
else:
    print("Введен некорректный номер")