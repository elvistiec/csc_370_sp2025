import numpy as np
import itertools
import time

def generate_random_graph(num_nodes, edge_prob):
    matrix = np.random.choice([0, 1], size=(num_nodes, num_nodes), p=[1 - edge_prob, edge_prob])
    np.fill_diagonal(matrix, 0)

    # Ensure at least one outgoing edge per node
    for i in range(num_nodes):
        if np.sum(matrix[i]) == 0:
            possible_targets = [j for j in range(num_nodes) if j != i]
            target = np.random.choice(possible_targets)
            matrix[i][target] = 1

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
            return True, perm
    return False, None

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

# Parameters
n = 10
edge_prob = 0.5
graph = generate_random_graph(n, edge_prob)

# Print adjacency matrix
print("Adjacency Matrix:")
print(graph)

# Check for existence of any Hamiltonian path
start_time = time.time()
has_path, first_path = has_hamiltonian_path(graph)
end_time = time.time()

print("\nHas Hamiltonian Path:", has_path)
print(f"Time taken: {end_time - start_time:.6f} seconds")

if has_path:
    print("First Hamiltonian Path Found:", " -> ".join(map(str, first_path)))

# Find and time all Hamiltonian paths
all_start = time.time()
all_paths = get_all_hamiltonian_paths(graph)
all_end = time.time()

print("\nAll Hamiltonian Paths:")
for path in all_paths:
    print(" -> ".join(map(str, path)))

print("\nTotal Hamiltonian Paths Found:", len(all_paths))
print(f"Time to find all paths: {all_end - all_start:.6f} seconds")