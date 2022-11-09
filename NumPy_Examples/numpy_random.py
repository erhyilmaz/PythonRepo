# NumPy Random Module examples
import numpy as np
from numpy import random

if 0:
    print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])

# x = random.randint(100)
x = random.randint(100, size=2)
# x = random.randint(100, size=(2, 5))
print(x)

# generate floating random numbers in [0,1] range
x = random.rand(2, 5)
print(x)


# choice() method takes an array as a parameter and randomly returns one of the values.
x = random.choice(arr)
print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))  # generate 3x5 matrix from the array elements
print(x)

# Distributions
# The choice() method allows us to specify the probability for each value.
# x = random.choice([1, 3, 5, 7], p=[0.1, 0.3, 0.6, 0.0], size=(20))
x = random.choice([1, 3, 5, 7], p=[0.1, 0.3, 0.4, 0.2], size=(6, 5))
print(x)

# The NumPy Random module provides two methods for this:
# - shuffle()
# - permutation()
print("Shuffle:")
print(arr)
random.shuffle(arr)  # shuffle() method makes changes to the original array
print(arr)

# permutation() method returns a re-arranged array (and leaves the original array un-changed)
print("Permutation:")
arr_perm = random.permutation(arr)
print(arr)
print(arr_perm)


