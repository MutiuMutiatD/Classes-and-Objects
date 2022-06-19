

from os import name


class Student:
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score
    
    def change_name(self, newname):
        self.name = newname
        print("My name is ", self.name)
    
    def change_age(self, newage):
        self.age = newage
        print("My age is ", self.age)

    def add_track(self, newtrack):
        self.track = newtrack
        print("I am enrolled in ", self.track)

    def get_score(self):
        print("My score is ", self.score)

Dami = Student(name="Dami", age=24, track="FullStack",score=36.92)

# Expected methods
Dami.change_name("Ife")
Dami.change_age(29)
Dami.add_track("FrontEnd")
Dami.get_score()
