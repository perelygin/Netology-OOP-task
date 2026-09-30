from models.Mentor import Mentor


class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)


    def __str__(self):  # Переопределение вывода объекта
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.countMiddleGrade():.2f}"