# File operations
# 2 options

# Option 1:
f = open("file.txt", "w")
content = f.read()
f.close()   # close() method shall be called!!!!


# Option 2:
with open("file.txt", "w") as f:
    content = f.read()
    # some other operations on the file, no need to call close() method









