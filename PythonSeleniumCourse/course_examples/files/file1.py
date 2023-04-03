import pdb

file_name = "./sample_files/sample.txt"

if 0:
    # demo 1
    f = open(file_name, "r")
    content = f.read()
    content_list = content.split('\n')[:-2]
    f.close()

    # demo 2
    f = open(file_name, "r")
    content = f.readlines()
    content_list = content.split('\n')[:-2]
    f.close()

# demo 3
f = open(file_name, "r")
content1 = f.read()
print(content1)
print("1---------------")
f.seek(0)
content2 = f.read()
print(content2)
print("2---------------")
f.close()

# pdb.set_trace()

