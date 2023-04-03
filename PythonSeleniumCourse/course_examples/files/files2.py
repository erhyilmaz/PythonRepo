import pdb

file_name = "./sample_files/countries.txt"

with open(file_name, "r") as f:
    # countries = f.read()
    countries = f.readlines()

print(countries)
# list_of_countries = countries.split('\n')
# print(list_of_countries)

list_of_countries = [i.strip() for i in countries]
print(list_of_countries)

# pdb.set_trace()

