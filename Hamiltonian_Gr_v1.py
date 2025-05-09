import numpy as np
import itertools
import time
from collections import defaultdict, deque

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

def find_hamiltonian_path(graph):
    n = len(graph)
    unvisted = set(range(n))
    path = []

    in_edges = [sum(graph[j][i] for j in range(n)) for i in range(n)]
    start = min(range(n), key=lambda x: in_edges[x])
    print("Starting node(count in computer science index):", start)
    curr = start
    path.append(curr)
    unvisted.remove(curr)

    while unvisted:
        attached = []
        for i in range(n):
            if (graph[curr][i] == 1) and (i in unvisted):

                unvisit_attached = sum(1 for j in range(n) if graph[i][j] == 1 and j in unvisted)
                attached.append((i, unvisit_attached))

        if not attached:
            return path, None
            return None
        #choose the next node with the least number of unvisited neighbors
        next_node = min(attached, key=lambda x: x[1])[0]
        path.append(next_node)
        unvisted.remove(next_node)
        curr = next_node

    return path
# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    n = 10
graph = generate_random_graph(n, 0.3)
print(graph)


print("Adjacency Matrix generated.")

start_time = time.time()
result = find_hamiltonian_path(graph) 
end_time = time.time()
print("Has Hamiltonian Path:", result)
print(f"Time taken: {end_time - start_time:.6f} seconds")