# example of 'random' module

import random

my_num = random.randint(100, 200)
print(my_num)
my_num = random.randrange(24)
print(my_num)
my_list = ['aaa', 'bbb', 'ccc', 'ddd']

# randomize a list
random.shuffle(my_list)
print(my_list)
my_list_ch = random.choice(my_list)
print(my_list_ch)





