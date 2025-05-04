import numpy as np
import itertools
import time

def generate_random_graph(num_nodes, edge_prob):
    matrix = np.random.choice([0, 1], size=(num_nodes, num_nodes), p=[1 - edge_prob, edge_prob])
    np.fill_diagonal(matrix, 0)
    return matrix

def has_hamiltonian_path(adj_matrix):
    num_nodes = len(adj_matrix)
    
    for perm in itertools.permutations(range(num_nodes)):
        valid_path = True
        for i in range(num_nodes - 1):
            if adj_matrix[perm[i]][perm[i + 1]] == 0:
                valid_path = False
                break
        if valid_path:
            return True
    return False

def get_all_hamiltonian_paths(adj_matrix):
    num_nodes = len(adj_matrix)
    paths = []
    
    for perm in itertools.permutations(range(num_nodes)):
        valid_path = True
        for i in range(num_nodes - 1):
            if adj_matrix[perm[i]][perm[i + 1]] == 0:
                valid_path = False
                break
        if valid_path:
            paths.append(perm)
    
    return paths

# WARNING: n > 10 becomes very slow due to factorial time
n = 8
graph = generate_random_graph(n, 0.3)
print("Adjacency Matrix generated.")

# Check for existence of any Hamiltonian path
start_time = time.time()
result = has_hamiltonian_path(graph)
end_time = time.time()
print("Has Hamiltonian Path:", result)
print(f"Time taken: {end_time - start_time:.6f} seconds")

# Find and print all Hamiltonian paths
