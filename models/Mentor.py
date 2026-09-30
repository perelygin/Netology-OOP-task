from models.Human import Human


class Mentor(Human):
    def __init__(self, name,surname: str):
        super().__init__(name, surname)
        self.courses_attached =[]


