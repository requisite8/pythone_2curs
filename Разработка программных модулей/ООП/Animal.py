
class Animal:
    def __init__(self, name=None, age=None, breed=None):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f'{self.name} {self.age} years old'

    def speak(self,sound):
        print(sound)