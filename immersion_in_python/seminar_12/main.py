import csv


class Student:
    def __init__(self, fio):
        self.fio = fio
        self.subjects = self.load_subjects()
        self.grades = {subject: [] for subject in self.subjects}
        self.test_results = {subject: [] for subject in self.subjects}

    def load_subjects(self):
        with open('subjects.csv', 'r') as file:
            reader = csv.reader(file)
            subjects = next(reader)
        return subjects

    @property
    def fio(self):
        return self._fio

    @fio.setter
    def fio(self, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError("ФИО должно содержать только буквы и начинаться с заглавной буквы.")
        self._fio = value

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет.")
        if grade < 2 or grade > 5:
            raise ValueError("Недопустимая оценка.")
        self.grades[subject].append(grade)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет.")
        if result < 0 or result > 100:
            raise ValueError("Недопустимый результат теста.")
        self.test_results[subject].append(result)

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет.")
        if len(self.test_results[subject]) == 0:
            return 0
        return sum(self.test_results[subject]) / len(self.test_results[subject])

    def overall_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            total_grades.extend(self.grades[subject])
        if len(total_grades) == 0:
            return 0

        print(total_grades)
        return sum(total_grades) / len(total_grades)


usr_student = Student("Иванов")


usr_student.add_grade("алгебра", 5)
usr_student.add_grade("литература", 5)
print(usr_student.grades)
print(usr_student.overall_average_grade())
