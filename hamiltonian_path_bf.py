# import itertools
# import random
# import numpy as np


# def generate_random_graph(num_nodes, edge_prob):
#     # Generate a random adjacency matrix with edge probabilities
#     matrix =  np.random.choice([0, 1], size=(num_nodes, num_nodes), p=[1 - edge_prob, edge_prob])
#     # Fill in diagonals with 0 so no vertices have paths to themselves
#     np.fill_diagonal(matrix, 0)
#     return matrix



# def take_connections(num_nodes, connections_list):



#     for i in range(num_nodes):

#         for j in range(len(connections_list)):

#             if connections_list[j] == None:
#                 break
#             if i == connections_list[j][0]:

#                 return

        


# def main():

#     graph = generate_random_graph(10, 0.9)
#     print(graph)

#     connections = [()]
#     for i, row in enumerate(graph):
        
#         for j, value in enumerate(row):

#             if i != j and value == 1:
                
#                 #print(f"Edge from node {i} to node {j}: {value}")

#                 connections.append((i, j))
    
    


#     print(connections)

# if __name__ == "__main__":
#     main()
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

# WARNING: n=100 will never complete using brute-force
n = 13
graph = generate_random_graph(n, 0.5)
print("Adjacency Matrix generated.")

start_time = time.time()
result = has_hamiltonian_path(graph)
end_time = time.time()

print("Has Hamiltonian Path:", result)
print(f"Time taken: {end_time - start_time:.6f} seconds")
