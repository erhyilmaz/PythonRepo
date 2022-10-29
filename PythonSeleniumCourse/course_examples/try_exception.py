# Example with exception

try:
    my_division = 20 / 0  # zero division!
    b = {'name': 'erhan', 'age': 30, 'job': 'Engineer'}
    c = b['weight']
except KeyError:
    print("Key Issue!")
except ZeroDivisionError:
    print("Zero Division Issue!")
except ValueError:
    print("Value Issue!")
finally:
    print("Do all the time")
