from Animal import Animal
class Cat():
    def __init__(self, name, age):
        super(),__init__(name, age)

    def __str__(self):
        return f'{self.name} is {self.age} year old'

    def speak(self,sound):
        print(sound)

cat1 = Cat("Djoric", 17)
cat2 = Cat("Marusya", 4)
print(cat1.__str__(),'\n',cat2.__str__())
cat1.speak('mya')
cat2.speak('mi')
