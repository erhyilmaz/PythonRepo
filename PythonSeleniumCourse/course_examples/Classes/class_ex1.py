class Animal:
    def __init__(self, color, food_type):
        print('This is init.')
        self.color = color
        self.food_type = food_type

    def move(self):
        print('Animal moves')

    def eat(self):
        print('Animal eats')
        print('This animal eats {}'.format(self.food_type))

    def main(self):
        self.move()
        self.eat()


my_animal = Animal('red', 'meat')
print(f"Color of my animal is {my_animal.color}")
print(f"Food type of my animal is {my_animal.food_type}")
my_animal.move()
my_animal.eat()
my_animal.main()
