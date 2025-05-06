import numpy as np
import itertools
import time
from collections import defaultdict, deque

def generate_random_graph(num_nodes, edge_prob):
    matrix = np.random.choice([0, 1], size=(num_nodes, num_nodes), p=[1 - edge_prob, edge_prob])
    np.fill_diagonal(matrix, 0)
    return matrix

def find_hamiltonian_path(graph):
    def dfs(node, visited, path):
        visited[node] = True
        path.append(node)

        # Get neighbors of the current node
        neighbors = [i for i, connected in enumerate(graph[node]) if connected and not visited[i]]

        # Sort neighbors by the number of unvisited neighbors they have (descending order)
        neighbors.sort(key=lambda x: sum(1 for i in range(len(graph)) if graph[x][i] and not visited[i]), reverse=True)

        for neighbor in neighbors:
            if dfs(neighbor, visited, path):
                return True

        # Backtrack if no Hamiltonian path is found
        if len(path) == len(graph):
            return True
        visited[node] = False
        path.pop()
        return False

    n = len(graph)
    visited = [False] * n
    path = []

    for start_node in range(n):
        if dfs(start_node, visited, path):
            return path

    return None  # No Hamiltonian path found

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    n = 4
graph = generate_random_graph(n, 0.3)
print(graph)
#graph = {
#    0: [1, 2],
#    1: [0, 2, 3],
#    2: [0, 1,3],
#    3: [1, 2]
#}
print("Adjacency Matrix generated.")

start_time = time.time()
result = find_hamiltonian_path(graph) 
end_time = time.time()
print("Has Hamiltonian Path:", result)
print(f"Time taken: {end_time - start_time:.6f} seconds")