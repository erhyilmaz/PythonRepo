# ----------------------
# Data Types in Python
# ----------------------
# By default Python have these data types:
#
#     strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
#     integer - used to represent integer numbers. e.g. -1, -2, -3
#     float   - used to represent real numbers. e.g. 1.2, 42.42
#     boolean - used to represent True or False.
#     complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
#
# ----------------------
# Data Types in NumPy
# ----------------------
# NumPy has some extra data types, and refer to data types with one character,
# like i for integers, u for unsigned integers etc.
#
# Below is a list of all data types in NumPy and the characters used to represent them.
#
#     i - integer
#     b - boolean
#     u - unsigned integer
#     f - float
#     c - complex float
#     m - timedelta
#     M - datetime
#     O - object
#     S - string
#     U - unicode string
#     V - fixed chunk of memory for other type ( void )
#
# ----------------------

# import numpy
import numpy as np

if 0:
    arr = np.array([1, 2, 3, 4])
    print(arr.dtype)

    arr = np.array(['apple', 'banana', 'cherry'])
    print(arr.dtype)

    arr = np.array([1, 2, 3, 4], dtype='S')
    print(arr)
    print(arr.dtype)

    # Change integer data type size
    arr = np.array([1, 2, 3, 4], dtype='i2')
    print(arr)
    print(arr.dtype)
    arr = np.array([1, 2, 3, 4], dtype='i4')
    print(arr)
    print(arr.dtype)
    arr = np.array([1, 2, 3, 4], dtype='i8')
    print(arr)
    print(arr.dtype)

    # Change data type from float to integer by using 'i' as parameter value
    arr = np.array([1.1, 2.1, 3.1])
    new_arr = arr.astype('i')  # or new_arr = arr.astype('int')
    print(arr)
    print(arr.dtype)
    print(new_arr)
    print(new_arr.dtype)

    # Change data type from int to boolean
    arr = np.array([1, 0, 3])
    new_arr = arr.astype(bool)
    print(new_arr)
    print(new_arr.dtype)

    # copy array: The copy SHOULD NOT be affected by the changes made to the original array.
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    arr[0] = 42
    print(arr)
    print(x)

    # view array: The view SHOULD be affected by the changes made to the original array.
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.view()  # view is as pointer in C/C++
    arr[0] = 42
    print(arr)
    print(x)

    # The original array SHOULD be affected by the changes made to the view.
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.view()  # view is as pointer in C/C++
    x[0] = 31
    print(arr)
    print(x)

    # Check if Array Owns its Data: NumPy array has the attribute base that returns None if the array owns the data.
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    y = arr.view()
    print(x.base)  # original
    print(y.base)  # view

    # Shape of an Array
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(arr.shape)

    arr = np.array([1, 2, 3, 4], ndmin=5)
    print(arr)
    print('shape of array :', arr.shape)

    # Reshape an Array
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print(arr)
    new_arr = arr.reshape(4, 3)
    print(new_arr)
    print('shape of array :', new_arr.shape)

    # 2D to 1-D reshape
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    new_arr = arr.reshape(-1)
    print(new_arr)
    print('shape of array :', new_arr.shape)

    # Joining NumPy Arrays
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.concatenate((arr1, arr2))
    print(arr)

    # Join two 2-D arrays along rows (axis=1)
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    arr = np.concatenate((arr1, arr2), axis=1)
    print(arr)

    # Joining Arrays Using Stack Functions
    # Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.stack((arr1, arr2), axis=1)
    print(arr)

    # Stacking Along Rows
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.hstack((arr1, arr2))
    print(arr)
    print(arr.shape)

    # Stacking Along Columns
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.vstack((arr1, arr2))
    print(arr)
    print(arr.shape)

    # Stacking Along Height (depth)
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.dstack((arr1, arr2))
    print(arr)
    print(arr.shape)

    # ----------------------------------
    # NumPy Array Iterating
    # ----------------------------------

    arr = np.array([1, 2, 3, 4, 5])
    for x in arr:
        print(x)

    # Iterating 2-D Arrays
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    for x in arr:
        print(x)

    for x in arr:
        for y in x:
            print(y)

    # Iterating 3-D Arrays
    arr = np.array([[[1, 2, 3], [4, 5, 6]],
                    [[7, 8, 9], [10, 11, 12]]])
    for x in arr:
        print(x)

    for x in arr:
        for y in x:
            for z in y:
                print(z)

    # ----------------------------------------
    # Iterating Arrays Using nditer()

    # Iterating on Each Scalar Element
    arr = np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]]])
    for x in np.nditer(arr):
        print(x)

    # Iterating Array With Different Data Types
    # We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
    # NumPy does not change the data type of the element in-place (where the element is in array)
    # so it needs some other space to perform this action, that extra space is called buffer,
    # and in order to enable it in nditer() we pass flags=['buffered'].
    arr = np.array([1, 2, 3])
    for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
        print(x)

    # Iterating With Different Step Size
    arr = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8]])
    for x in np.nditer(arr[:, ::2]):
        print(x)

    # Enumerated Iteration Using ndenumerate()
    # Enumeration means mentioning sequence number of somethings one by one.
    # Sometimes we require corresponding index of the element while iterating,
    # the ndenumerate() method can be used for those usecases.
    arr = np.array([1, 2, 3])
    for idx, x in np.ndenumerate(arr):
        print(idx, x)

    arr = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8]])
    for idx, x in np.ndenumerate(arr):
        print(idx, x)

    # ---------------------------------------------
    # Splitting NumPy Arrays:
    # - array_split()
    # - hsplit() [opposite of hstack()]
    # - vsplit() [opposite of vstack()]
    # - dsplit() [opposite of dstack()]
    # ---------------------------------------------
    # array_split() method is used for splitting arrays,
    # we pass it the array we want to split and the number of splits.
    # arr = np.array([1, 2, 3, 4, 5, 6])
    # arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    new_arr = np.array_split(arr, 3)
    # new_arr = np.array_split(arr, 3, axis=1)
    print(new_arr[0])
    print(new_arr[1])
    print(new_arr[2])

# ---------------------------------------------
# Searching Arrays: search an array for a certain value, and return the indexes that get a match.
# - where()
# - searchsorted()
# ---------------------------------------------
#

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)  # will return a tuple
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 0)
# x = np.where(arr % 2 == 1)
print(x)

# searchsorted() which performs a binary search in the array,
# and returns the index where the specified value would be inserted to maintain the search order.
# The searchsorted() method is assumed to be used on sorted arrays.
# By default the left most index is returned,
# but we can give side='right' to return the right most index instead.
arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7) # default 'left' sided search
# x = np.searchsorted(arr, 7, side='left')
x = np.searchsorted(arr, 7, side='right')
print(x)

# Search multiple values
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])  # Find the indexes where the values 2, 4, and 6 should be inserted
print(x)








