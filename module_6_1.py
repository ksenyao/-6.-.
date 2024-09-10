class Animal:
    alive = True  # живой
    fed = False  # накормленный

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False  # съедобность

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):
    edible = True

    def __init__(self, name):
        super().__init__(name)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)