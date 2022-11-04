# NumPy examples

# import numpy
import numpy as np

if 0:
    print(np.__version__)

    # To create an ndarray, we can pass a list, tuple or any array-like object into the array() method,
    # and it will be converted into an ndarray
    # arr = numpy.array([1, 2, 3, 4, 5])
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    print(type(arr))
    arr = np.array((6, 7, 8, 9, 10))
    print(arr)
    print(type(arr))

    arr = np.array(42)  # 0-D arrays, or Scalars
    print(arr.ndim)
    print(type(arr))

    arr2D = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr2D)
    print(arr2D.ndim)
    print(type(arr2D))

    arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
    print(arr3D)
    print(arr3D.ndim)
    print(type(arr3D))

    # Create an array with 5 dimensions and verify that it has 5 dimensions
    arr5D = np.array([1, 2, 3, 4], ndmin=5)
    print(arr5D)
    print('number of dimensions :', arr5D.ndim)

arr = np.array([1, 2, 3, 4, 5])
print(arr[0] + arr[4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on 1st row: ', arr[0, 1])
print('4th element on 2nd row: ', arr[1, 3])

arr = np.array([[[1, 2, 3],
                 [4, 5, 6]],
                [[7, 8, 9],
                 [10, 11, 12]]])

print(arr[0, 1, 2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Last element from 2nd dim: ', arr[1, -1])  # negative indexing

# Slicing arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])
print(arr[4:6])
print(arr[0:6:2])
print(arr[-3:-1])
print(arr[::2])  # return every other element of the array

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
