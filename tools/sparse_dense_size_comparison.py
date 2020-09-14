# Compare memory usage of a dense and a sparse adjancency matrix.
#
# Requires numpy. Install it with `pip3 install --user numpy`
# Authors: Gianluca Andreotti, Aurora Lucrezia Castro

import numpy as np

from scipy.sparse import csr_matrix
import sys


def load_matrix(file):
    matrix = np.loadtxt(file, dtype=int, ndmin=2)
    print("Nodes: " + str(len(matrix)))
    print(f"Dense matrix: {matrix.nbytes / 1000}mb")
    sparse_csr_mat = csr_matrix(matrix)
    print(f"Sparse matrix: {sparse_csr_mat.data.nbytes / 1000}mb")
    print("")


if __name__ == "__main__":
    for f in sys.argv[1:]:
        load_matrix(f)
