# Tool for generating adjacency matrix of arbitrary size
#
# Requires numpy. Install it with `pip3 install --user numpy`
# Authors: Gianluca Andreotti, Aurora Lucrezia Castro

# Graph settings
sizes = (10, 50, 100, 500, 1000, 5000, 10000, 15000, 20000)

# Make it reproducible
seed = 0

import random, numpy


def rand_adj_matrix(n_nodes, oriented=False, max_weight=9):
    # Make it reproducible
    random.seed(seed)

    # Use Numpy to speed up matrix creation and operations
    adj_matrix = numpy.zeros((n_nodes, n_nodes), dtype=int)

    for x in range(n_nodes):
        for y in range(0, x):
            if x == y:
                continue

            # Randomly chose between 0 and a weight
            # Is there a better way to do this?
            weight = random.choice([0, random.randint(1, max_weight)])
            adj_matrix[x][y] = weight

            if not oriented:
                # Make the edge bidirectional
                adj_matrix[y][x] = adj_matrix[x][y]

    return adj_matrix


if __name__ == "__main__":
    for size in sizes:
        adj = rand_adj_matrix(size)
        numpy.savetxt(f"adj-{size}-nodes.txt", adj, fmt="%2u")
