# %%
import numpy as np
a = np.array([1, 2, 3])
a

# %%
# Do a sequence of numbers with arange
np.arange(10)

# %%
# Multiply sequence by a scalar
np.arange(10) * np.pi

# %%
# Make multi-dimensional array from single dimensions with shape
a = np.array([1, 2, 3, 4, 5, 6])
a.shape = [2,3]
a

# %%
# Make a matrix
np.matrix('1 2; 3 4')

# %%
# Matrix multiplication requires the use of matrices
a1 = np.matrix('1 2; 3 4')
a2 = np.matrix('3 4; 5 7')
a1 * a2

# %%
# Converting an array to a matrix
mat_a = np.mat(a)
mat_a

# %%
type(a)

# %%
type(a1)

# %%
type(mat_a)

# %%
# Load sparse data into a sparse matrix
import numpy, scipy.sparse
n = 100000
x = (numpy.random.rand(n) * 2).astype(int).astype(float) # 50% sparse vector
x_csr = scipy.sparse.csr_matrix(x)
x_dok = scipy.sparse.dok_matrix(x.reshape(x_csr.shape))

x_dok
# %%
# Load a numpy array from a file
import csv
with open('array.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    data = []
    for row in csvreader:
        row = [float(x) for x in row]
        data.append(row)

data
# %%
# Solving a matrix
import numpy as np
import scipy as sp
a = np.array([[3,2,0],[1,-1,0],[0,5,1]])
b = np.array([2,4,-1])
x = np.linalg.solve(a,b)
x

# %%
# Checking the answer
np.dot(a, x) == b

# %%
