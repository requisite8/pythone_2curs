class Dog:
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f'This {self.breed} - {self.name} is {self.age} year old'

    def speak(self,sound):
        print(sound)