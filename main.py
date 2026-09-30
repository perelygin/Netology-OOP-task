from models.Lecturer import Lecturer
from models.Mentor import Mentor
from models.Reviewer import Reviewer
from models.Student import Student


def avrStudentGrade(students,curseName):
    GlobalGrades=[]
    for student in students:
        for course in student.grades:
            if course == curseName:
                if student.grades[course]:
                    GlobalGrades.extend(student.grades[course])
                else:
                    return 'Ошибка. Пустой список'
    return sum(GlobalGrades)/len(GlobalGrades)



def avrLectrersGrade(lecturers,curseName):
    GlobalGrades = []
    for lecturer in lecturers:
        for course in lecturer.grades:
            if course == curseName:
                if lecturer.grades[course]:
                    GlobalGrades.extend(lecturer.grades[course])
            else:
                return 'Ошибка. Пустой список'
    return sum(GlobalGrades) / len(GlobalGrades)

students = []
lecturers = []

lecturer1 = Lecturer('Иван', 'Иванов')
lecturers.append(lecturer1)
reviewer1 = Reviewer('Пётр', 'Петров')
student1  = Student('Алёхина', 'Ольга', 'Ж')
students.append(student1)


student1.courses_in_progress += ['Python', 'Java', 'C++']
lecturer1.courses_attached += ['Python', 'C++']
reviewer1.courses_attached += ['Python', 'C++']

lecturer2 = Lecturer('Хуан', 'Санчес')
lecturers.append(lecturer2)
reviewer2 = Reviewer('Педро', 'Мурано')
student2  = Student('Алёхин', 'Олег', 'М')
students.append(student2)

student2.courses_in_progress += ['Python', 'Java', 'C++']
lecturer2.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Python', 'C++']




student1.rate_lecture(lecturer1, 'Python', 7)  # None
student1.rate_lecture(lecturer1, 'Python', 8)  # Ошибка
student1.rate_lecture(lecturer1, 'С++', 8)  # Ошибка
student1.rate_lecture(lecturer1, 'Python', 6)  # Ошибка
student2.rate_lecture(lecturer2, 'Python', 3)  # None
student2.rate_lecture(lecturer2, 'Python', 2)  # Ошибка
student2.rate_lecture(lecturer2, 'С++', 4)  # Ошибка
student2.rate_lecture(lecturer2, 'Python', 5)  # Ошибка

reviewer1.rate_hw(student1,  'Python', 3)
reviewer1.rate_hw(student1,  'Python', 4)
reviewer1.rate_hw(student1,  'C++', 3)
reviewer2.rate_hw(student2,  'Python', 7)
reviewer2.rate_hw(student2,  'Python', 9)
reviewer2.rate_hw(student2,  'C++', 3)

# print(f"Оценки лектора 1 {lecturer1.grades}")  # {'Python': [7]}
# print(f"Оценки лектора 2 {lecturer2.grades}")
# print(f"Оценки Студента 1 {student1.grades}")
# print(f"Оценки Студента 2 {student2.grades}")
# print("---------- преподы ----------")
# print(lecturer1)
# print(lecturer2)
# print(lecturer1>=lecturer2)
# print(lecturer1<=lecturer2)
#
# print("---------- студенты ----------")
# print(student1)
# print(student2)
#
# print(student1>student2)
# print(student1>=student2)
# print(student1<=student2)

#print(student1>lecturer1)

print(avrStudentGrade(students,'Python'))
print(avrLectrersGrade(lecturers,'Python'))