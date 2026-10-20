from Animal import Animal


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)

    def __str__(self):
        return f'This {self.breed} - {self.name} is {self.age} year old'

    def speak(self, sound):
        print(f'{self.name} the dog says: {sound}')


if __name__ == "__main__":
    dog1 = Dog("Rex", 5, "husky")
    dog2 = Dog("Bobik", 2, "corgi")
    print(dog1, '\n', dog2)
    dog1.speak('woof')
    dog2.speak('gav')
