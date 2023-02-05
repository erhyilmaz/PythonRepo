# -------------------------------------------------------------
# -------------------------------------------------------------
# TUPLES are Immutable but more efficient to use
# -------------------------------------------------------------
# -------------------------------------------------------------

# -------------------------------------------------------------
# -------------------------------------------------------------
# The top 10 most common words in a file
# -------------------------------------------------------------
# -------------------------------------------------------------
# fname = input('Enter a file name: ')
fname = 'deneme.txt'
fhandle = open(fname)   # open file

counts = dict()   # or use: counts = { }
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for k, v in counts.items():
    newtuple = (v, k)  # flip key and value positions
    lst.append(newtuple)
    lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)


# -------------------------------------
# A short version of sorting tuple
# -------------------------------------
c = {'a': 10, 'b': 1, 'c': 21, 'd': 8}
print(sorted([(v, k) for k, v in c.items()]))  # list comprehension




