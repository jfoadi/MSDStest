###
## Seconf Py file
###

# Creates two random 3X3 matrices and add them up

import numpy as np

# Create two random 3X3 matrices
matrix1 = np.random.rand(3, 3)  
matrix2 = np.random.rand(3, 3)

# Add the two matrices
result = matrix1 + matrix2

# Print the results
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nResult of Matrix 1 + Matrix 2:")
print(result)