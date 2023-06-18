from intro_python.seminar_8.task_38.functions import *
from os.path import exists


def main():
    while True:
        step = input("Введите действие:\nq - выйти из меню\nw - запись в файл\ns - поиск по файлу\nd - удалить контакт\nс - изменить контакт\nr - чтение всего файла\nДействие: ")
        match step:
            case "q":
                break
            case "r":
                view()
            case "s":
                search_contact()
            case "d":
                delete_contact()
            case "c":
                change_contact()
            case "w":
                path = 'phone.csv'
                flag = exists(path)
                if not flag:
                    creating()
                    record_info()
                else:
                    record_info()


main()
