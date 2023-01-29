# -------------------------------------------------------------
# -------------------------------------------------------------
# Counting Pattern with dictionaries:
# 1 - As opposed to lists, dictionaries are not ordered
# 2 - syntax: dict = { 'key1': val1, 'key2': val2, ... }
# 3 - if we try to access a key which does not exist in the dict than we get KeyValue Error
# 4-
# -------------------------------------------------------------
# -------------------------------------------------------------
if 0:
    counts = dict()
    print('Enter a line of text: ')
    line = input('')
    words = line.split()
    print('Words:', words)

    print('Counting....')
    if 0:
        # 1st way:
        for word in words:
            if word not in counts:  # use of 'not' and 'in' reserved words
                counts[word] = 1
            else:
                counts[word] = counts[word] + 1
    else:
        # 2nd way:
        for word in words:
            counts[word] = counts.get(word, 0) + 1  # simplify counting with get() method
    print('Counts', counts)

    # print(list(counts))
    # print(counts.keys())
    # print(counts.values())
    # print(counts.items())

    # Two Iteration Variables
    for k, v in counts.items():
        print(k, v)


# -------------------------------------------------------------
# -------------------------------------------------------------
# Count Words in a file and the most frequent one
# -------------------------------------------------------------
# -------------------------------------------------------------
# fname = input('Enter a file name: ')
fname = 'deneme.txt'
fhandle = open(fname)   # open file

counts = dict()   # or use: counts = { }
for line in fhandle:
    words = line.upper().split()  # case in sensitive search
    for word in words:
        counts[word] = counts.get(word, 0) + 1  # use of get() method and fill dict keys with words' histogram values

max_freq_word = None  # use of None
max_freq_count = None
for word, count in counts.items():  # use of two iteration variable with item() method
    print(word, count)
    if max_freq_count is None or count > max_freq_count:
        max_freq_word = word
        max_freq_count = count

print(max_freq_word, max_freq_count)







