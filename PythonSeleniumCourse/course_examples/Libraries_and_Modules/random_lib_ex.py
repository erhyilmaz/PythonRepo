# example of 'random' module
import random

my_num = random.randint(100, 200)
print(my_num)

# generate float random variable in [0,1] interval
x = random.uniform(0, 1)
print(x)

# generate float random variable in [0,1] interval
my_num = random.randrange(0, 24)
print(my_num)

my_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']

# randomize a list
random.shuffle(my_list)
print(my_list)

# choice() method: allows you to generate a random value based on an array of values.
my_list_ch = random.choice(my_list)
print(my_list_ch)





