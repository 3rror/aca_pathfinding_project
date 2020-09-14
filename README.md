# Parallel pathfinding

Project of Advanced Computer Architecture at University of Pavia.

## Goal

Parallelize some common pathfinding algorithms using OpenMP and shared memory.

## Generate input data

- Install **Python 3.x** if you don't have it
- Install NumPy:

```python
pip3 install numpy
```

- Run adj_matrix_generator.py

```python
python3 tools/adj_matrix_generator.py
```

## Compile the source code

- Install **cmake**
- Run

```
cmake .
```

- And then run

```
make
```

## Execute the program

```sh
./aca_pathfinding adj-N-nodes.txt
```

## Authors

- Gianluca Andreotti
- Aurora Lucrezia Castro
