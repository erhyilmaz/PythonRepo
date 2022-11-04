# Dictionaries (counterpart of struct in C/C++)
# - Not sequenced (no indexing)
# - Mutable (can be appended new elements)
# - syntax:  { key1: value1 [, key2: value2,] }
# - any data type can be a 'Value'
# - any immutable data type can be 'Key'
# val = dict_name[key]
# val = dict_name.get(key)
# val = dict_name.get(key, <default>)
# dict_name[key] = val

# example 1
family = {"Father": "Ali", "Mother": "Ayse", "Son": "Veli", "Elder Daughter": "Zeynep"}
print(family)

# get key value
my_son = family["Son"]
print(my_son)
my_son = family.get("Son")
print(my_son)
# my_son = family["Aunt"]  # will fail : KeyError
my_son = family.get("Aunt")  # if not exists, returns 'None'
print(my_son)
my_son = family.get("Aunt", "N/A")  # default usage: if not exists, returns 'N/A'
print(my_son)

# add a new key to the dictionary
family["Younger Daughter"] = "Elif"
print(family)
family.update({"Uncle": "Mehmet"})
print(family)

print("-------------------------------------------------------")

# add a new key to the dictionary with default option, if the key is in the dict that its value is returned,
# otherwise the default value is returned
family_grandfather = family.setdefault("dede", "Ahmet")  # update the dict and return Ahmet
print(family_grandfather)
family_grandfather = family.setdefault("Uncle", "Mustafa")  # 'Uncle' already in the dict, hence return that value
print(family_grandfather)
print(family)

print("-------------------------------------------------------")

# --------------------------------------------
# Methods for dictionary
# dict_name.get(Key)  and dict_name.update({Key: Val})
# dict_name.values()  and dict_name.keys()
# class 'dict_values' and class 'dict_keys' are iterable types
family_names = family.values()
print(family_names)
print(type(family_names))

family_keys = family.keys()
print(family_keys)
print(type(family_keys))








