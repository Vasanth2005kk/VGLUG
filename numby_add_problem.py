import numpy  # Import the NumPy library for array operations

# Create two 2D NumPy arrays
arr = numpy.array([[1, 2, 3], [4, 5, 6]])
arr_1 = numpy.array([[10, 20, 30], [40, 50, 60]])

# Get the shapes of both arrays and convert them to lists
a, b = list(arr.shape), list(arr_1.shape)

# Check if the shapes of both arrays are the same
if a == b:
    # If they are the same, perform element-wise addition of the two arrays
    output = arr + arr_1
    # Print the resulting array
    print(output)
