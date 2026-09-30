from models.Human import Human
from models.Lecturer import Lecturer


class Student(Human):
    def __init__(self, name, surname,gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer,course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):  # Переопределение вывода объекта
        return (f"Имя: {self.name} "
                f"\nФамилия: {self.surname} "
                f"\nСредняя оценка за домашние задания:{self.countMiddleGrade():.2f} "
                f"\nКурсы в процессе изучения:{self.courses_in_progress}"
                f"\nЗавершенные курсы:{self.finished_courses}"
                f"\nКурсы в процессе изучения:{self.courses_in_progress}"
                f"\nЗавершенные курсы:{self.finished_courses}"
                )
