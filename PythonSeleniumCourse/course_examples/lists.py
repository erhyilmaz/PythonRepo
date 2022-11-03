# Lists are MUTABLE (CHANGEABLE) sequenced data type
# Arrays in C/C++, Java, etc.
# Each element are separated by comma
# Lists can contain several data types!!
# Indexing applies for lists
# Index starts from  0 going left to right
#              from -1 going right to left
#
my_list = [12, 12.5, 'Erhan', '0.4', 305, '$14']
print(type(my_list))
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[0:])
print(my_list[0:3])     # index 3 in not included!
print(my_list[0:0])     # index 0 in not included: empty list!
print(my_list[-3:])     # last 3 elements
print(my_list[-3:-1])   # the last element is not included! 2 elements are return

my_list = ['car', 'Boat', 'House', 'plane', 'train']
x = my_list[0:]
print(x)
x = my_list[1:]
print(x)
y = my_list[1:3]
print(y)
print("------------------------")

# ---------------------------------------
# List Methods (Functions)
my_list = ['car', 'Boat', 'House', 'plane', 'train']
print(len(my_list))
my_list.append('ship')  # append a new element to the end of the list
print(my_list)
x = my_list.pop()  # remove the last element from the list
print(x)
print(my_list)
my_list.remove('Boat')  # remove an element from the list
print(my_list)


















