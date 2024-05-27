
class Dog():

    all = []

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        Dog.all.append(self)


dog1 = Dog('mya', 12, 'Golden')
dog2 = Dog('Max', 2, 'pitbull')

dog1.name = 'Buddy'
print(dog1.name)

