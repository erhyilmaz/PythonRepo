file_name = "./sample_files/output.txt"
my_string = "My name is Yilmaz"

if 0:
    # ex 1
    f = open(file_name, "w")
    f.write(my_string)
    f.close()

    # ex 2
    f = open(file_name, "w")
    f.write(my_string + '\n')
    f.write(my_string)
    f.write('\n')
    f.write(my_string)
    f.close()

    # ex 3
    with open(file_name, "w") as f:
        f.write(my_string + '\n')
        f.write(my_string)

    # ex 4
    my_list = ['user 1', 'user 2', 'user 3']
    with open(file_name, "w") as f:
        for i in my_list:
            f.write(i + '\n')

    # ex 5 appending
    my_list = ['append 1', 'append 2', 'append 3']
    with open(file_name, 'a') as f:
        for i in my_list:
            f.write(i + '\n')

# ex 6: string split() and join() methods
my_list = ['join 1', 'join 2', 'join 3']
with open(file_name, 'w') as f:
    # f.writelines(';'.join(my_list))
    f.write('\n'.join(my_list))

