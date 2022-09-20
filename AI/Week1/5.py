# In mathematics, a matrix (plural matrices) is a rectangular array or table of
# numbers, symbols, or expressions, arranged in rows and columns. In mathematics,
# a square matrix is a matrix with the same number of rows and columns. In linear
# algebra, the trace of a square matrix A is defined to be the sum of elements on the
# main diagonal (from the upper left to the lower right).
# Example: A= [
#  [0, 1, 0, 0],
#  [1, 1, 1, 1],
#  [0, 1, 0, 1],
#  [0, 1, 1, 5]
# ]
# tr(A)=6

import numpy as np

mx = np.array([[0, 1, 0, 0],[1, 1, 1, 1],[0, 1, 0, 1],[0, 1, 1, 5]])
print(mx.trace())