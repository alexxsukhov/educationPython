import csv


def search_contact():
    usr_query = input("Введите фамилию, имя или телефон для поиска: ")
    file = "phone.csv"

    with open(file, "r", newline="", encoding='utf-8') as data:
        for row in data:
            if usr_query.lower() in row.lower():
                print(f"{row}")
        else:
            print("Контакты не найдены")


def validate_phone():
    phone_number = ''
    flag = False
    while not flag:
        try:
            phone_number = input("Введите номер: ")
            if len(phone_number) != 11:
                print("В номере должно быть 11 цифр")
            else:
                phone_number = int(phone_number)
                flag = True

        except:
            print("В номере должны быть только цифры")

    return phone_number


def change_contact():
    usr_query = input("Введите номер телефона: ")
    file = "phone.csv"
    with open(file, "r", newline="", encoding='utf-8') as data:
        reader = csv.reader(data)
        lines = list(reader)

    for line in lines:
        if line[2] == usr_query:
            print("Введите новые данные для контакта.")
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")

            phone_number = validate_phone()

            line[0] = last_name
            line[1] = first_name
            line[2] = phone_number

    with open(file, "w", newline="", encoding='utf-8') as data:
        writer = csv.writer(data)
        writer.writerows(lines)


def delete_contact():
    usr_query = input("Введите номер телефона: ")
    file = "phone.csv"
    with open(file, "r", newline="", encoding='utf-8') as data:
        reader = csv.reader(data)
        lines = list(reader)

    lines = [line for line in lines if line[2] != usr_query]

    with open(file, "w", newline="", encoding='utf-8') as data:
        writer = csv.writer(data)
        writer.writerows(lines)


def creating():
    file = "phone.csv"
    with open(file, "w", encoding='utf-8') as data:
        data.write(f"Фамилия,Имя,Номер\n")


def writing_csv(info):
    file = "phone.csv"
    with open(file, 'a', newline="", encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]}\n')


def reading_csv(file):
    with open(file, encoding='utf-8') as data:
        res = list(csv.DictReader(data))
    return res


def get_info():
    info = []
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    info.append(last_name)
    info.append(first_name)

    phone_number = validate_phone()

    info.append(phone_number)
    return info


def record_info():
    info = get_info()
    writing_csv(info)


def view():
    views_list = reading_csv('phone.csv')
    for row in views_list:
        print(row)
