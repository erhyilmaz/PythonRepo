string = "     Hello World, My name is Erhan     "

print(string)
string_strip = string.strip()
print(string_strip)
string_upper = string_strip.upper()
print(string_upper)
string_lower = string_strip.lower()
print(string_lower)

# string_split = string_strip.split()
string_split = string_strip.split(" ")  # the same as above
string_split = string_strip.split(",")
print(string_split)
# string_count = string_strip.count('e')
string_count = string_strip.lower().count('e')
print(f"Count of letter 'e' is {string_count}")
string_len = len(string_strip)
# print(string_len)
print(f"Length of the string is {string_len}")

string_end_bool = string_strip.endswith("n")
print(f"Does the sting end with 'n' ? {string_end_bool}")

# string_strip.startswith("A")
# string_strip.isalnum()
# string_strip.isdecimal()
# string_strip.count("Erhan")  # return the number of non-overlapping occurrences of substring
# string_strip.expandtabs(tabsize=4)

# -----------------------------------------------------------
ssn = "1111-2222-3333-4444"
ssn_s = ssn.split('-')
print(ssn)
print(ssn_s)

# -----------------------------------------------------------
sss = ".....abcde\nfghi......"
sss_s = sss.strip('.')
print(sss)
print(sss_s)

# -----------------------------------------------------------
url = 'https:\\abc.com/'
is_url = url.endswith('.com/')
print(f"Is {url} a valid home page ?  {is_url}")

# -----------------------------------------------------------
info = "This%20is%20url%20encoded"
info_replace = info.replace("%20", " ")
print(info_replace)

# -----------------------------------------------------------
print("{} is age {} years old".format("Erhan", 39))
print("{0} is age {1} years old".format("Erhan", 39))
print("{name} is age {age} years old".format(name="Erhan", age=39))
name, age = "Erhan", 39
print(f"{name} is age {age} years old")
print(f"There are {len('Python')} letters in 'Python'")










