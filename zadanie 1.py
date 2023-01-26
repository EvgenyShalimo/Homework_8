import time


class Auto:
    def __init__(self, brand, age, mark, color='red', weight='200kg'):
        print(self, brand, age, mark, color, weight)
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('MOVE!!!')

    def stop(self):
        print('STOOOOOP!!!')

    def birhday(self):
        self.age += 1
        return print(self.age)


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color='red', weight='200kg'):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('ATTENTION!!!')
        super().move()
        return self

    def load(self):
        time.sleep(1)
        print('Load...')
        time.sleep(1)
        return self


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color='red', weight='200kg'):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        print(f'max speed is {self.max_speed}')
        return self


car1 = Truck('LEXUS', 22, 'c7', '220 km')
print('Class Truck')
car1.birhday()
car1.load()
car1.move()
car1.stop()
print('Mark:', car1.mark, '\nBrand:', car1.brand, '\nAge:', car1.age, '\nMark:', car1.mark, '\nMax_Load:',
      car1.max_load, '\nColor:', car1.color, '\nweight:', car1.weight)

car2 = Car('BVM', 14, 'a5', '300 km/ch')
print('Class Car')
car2.birhday()
car2.move()
car2.stop()
print('Mark:', car2.mark, '\nBrand:', car2.brand, '\nAge:', car2.age, '\nMark:', car2.mark, '\nMax_SPEED:',
      car2.max_speed, '\nColor:', car2.color, '\nweight:', car2.weight)
