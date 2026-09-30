class Human:
    """
    базовый класс для Студентов и Преподавателей.
    """
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    def grades(self):
        return self.grades


    """
        Метод вычисляет среднюю оценку 
    """
    def countMiddleGrade(self):
        mid_val = 0
        if self.grades:
            count = 0
            amount = 0
            for gradeList in self.grades.values():
                count += len(gradeList)
                amount += sum(gradeList)
            mid_val = amount / count
        return mid_val

    def __eq__(self, other):
        if not isinstance(other, Human):
            return NotImplemented
        if type(self) != type(other):
            return NotImplemented
        return self.countMiddleGrade() == other.countMiddleGrade()

    def __ne__(self, other):
        if not isinstance(other, Human):
            return NotImplemented
        if type(self) != type(other):
            return NotImplemented
        return self.countMiddleGrade() != other.countMiddleGrade()

    def __lt__(self, other):
        if not isinstance(other, Human):
            return NotImplemented
        if type(self) != type(other):
            return NotImplemented
        return self.countMiddleGrade() < other.countMiddleGrade()


    def __gt__(self, other):
        if not isinstance(other, Human):
            return NotImplemented
        if type(self) != type(other):
            return NotImplemented
        return self.countMiddleGrade() > other.countMiddleGrade()

    def __le__(self, other):
        if not isinstance(other, Human):
            return NotImplemented
        if type(self) != type(other):
            return NotImplemented
        return self.countMiddleGrade() <= other.countMiddleGrade()

    def __ge__(self, other):
        if not isinstance(other, Human):
            return NotImplemented
        if type(self) != type(other):
            return NotImplemented
        return self.countMiddleGrade() >= other.countMiddleGrade()