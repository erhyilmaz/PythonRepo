# Check :  https://docs.python.org/3/library/re.html

import re   # import regular expression library

data = "From erhan.yilmaz@airspan.com Sun Feb 5 21:06:15 2023"

# 1st Way
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)

# 2nd Way
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# 3rd Way: Regular Expressions
y = re.findall('@([^ ]*)', data)
print(y)

# 4th Way: Regular Expressions
y = re.findall('^From .*@([^ ]*)', data)
print(y)

# --------------------------------------------------------
# --------------------------------------------------------

x = "We just received $10.00 for cookies."
y = re.findall('\$[0-9.]+', x)
print(y)

