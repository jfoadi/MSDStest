###
## Fourth Py file
###

# Multiply two random 2X2 matrices

import numpy as np

# Create two random 2X2 matrices
matrix1 = np.random.rand(2, 2)
matrix2 = np.random.rand(2, 2)

# Multiply the two matrices
result = np.dot(matrix1, matrix2)

# Print the results
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nResult of Matrix 1 * Matrix 2:")
print(result)