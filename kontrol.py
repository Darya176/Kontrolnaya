#задание 16
class Bot():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, string):
        if self.x >100 or self.x < 0 or self.y > 100 or self.y <0:
            return 'таких координат не существует'
        else:
            for i in string:
                if i == 'N':
                    self.y += 1
                    if self.y > 100:
                        self.y = 100

                if i == 'S':
                    self.y -= 1
                    if self.y < 0:
                        self.y = 0

                if i == 'E':
                    self.x += 1
                    if self.x > 100:
                        self.x = 100

                if i == 'W':
                    self.x -= 1
                    if self.x < 0:
                        self.x = 0

                list = [self.x, self.y]

        return list

object1 = Bot(10, 15)
print(object1.move('NNSEEW'))

object1 = Bot(100, 100)
print(object1.move('NNSEEW'))

object1 = Bot(101, -1)
print(object1.move('NNSEEW'))

