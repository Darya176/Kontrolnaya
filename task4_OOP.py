#задача 4

class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.elephant >= self.bee:
            return 'tu-tu-doo-doo'
        else:
            return 'wzzzz'

    def eat(self, meal, value):
        self.meal = meal
        self.value = value
        if meal == 'nectar':
            self.elephant -= value
            if self.elephant < 0:
                self.elephant = 0
            self.bee += value
            if self.bee > 100:
                self.bee = 100

        else:
            self.elephant += value
            if self.elephant > 100:
                self.elephant = 100
            self.bee -= value
            if self.bee < 0:
                self.bee = 0
        return self.bee, self.elephant

    def get_parts(self):
        list = [self.bee, self.elephant]
        return list




animal = BeeElephant(45,55)
print(animal.fly())
print(animal.trumpet())
print(animal.eat('nectar', 100))
print(animal.get_parts())
print(animal.eat('grass', 25))
print(animal.get_parts())

animal_1 = BeeElephant(60,5)
print(animal_1.fly())
print(animal_1.trumpet())
print(animal_1.eat('nectar', 100))
print(animal_1.get_parts())
print(animal_1.eat('grass', 25))
print(animal_1.get_parts())