import numpy as np
import itertools
import time
import matplotlib.pyplot as plt

def generate_random_graph(num_nodes, edge_prob):
    matrix = np.random.choice([0, 1], size=(num_nodes, num_nodes), p=[1 - edge_prob, edge_prob])
    np.fill_diagonal(matrix, 0)

    if num_nodes > 1:
        for i in range(num_nodes):
            if np.sum(matrix[i]) == 0:
                possible_targets = [j for j in range(num_nodes) if j != i]
                if possible_targets:
                    target = np.random.choice(possible_targets)
                    matrix[i][target] = 1

    return matrix

def find_hamiltonian_path_greedy(graph):
    n = len(graph)
    unvisited = set(range(n))
    path = []

    in_edges = [sum(graph[j][i] for j in range(n)) for i in range(n)]
    start = min(range(n), key=lambda x: in_edges[x])
    curr = start
    path.append(curr)
    unvisited.remove(curr)

    while unvisited:
        attached = []
        for i in range(n):
            if graph[curr][i] == 1 and i in unvisited:
                unvisited_attached = sum(1 for j in range(n) if graph[i][j] == 1 and j in unvisited)
                attached.append((i, unvisited_attached))

        if not attached:
            return None

        next_node = min(attached, key=lambda x: x[1])[0]
        path.append(next_node)
        unvisited.remove(next_node)
        curr = next_node

    return path

def has_hamiltonian_path_bruteforce(adj_matrix):
    num_nodes = len(adj_matrix)
    for perm in itertools.permutations(range(num_nodes)):
        if all(adj_matrix[perm[i]][perm[i + 1]] == 1 for i in range(num_nodes - 1)):
            return True, perm
    return False, None

# test runs
max_seconds = 600 # timeout at 10 minutes
edge_prob = 0.5
n = 2 # start at 2 nodes
node_counts = []
greedy_times = []
brute_times = []

# export results file
with open("results.txt", "w") as f:
    
    f.write("node_number\tgreedy_time\tbrute_time\tgreedy_path\tbrute_path\n")

    while True:
        print(f"\n{n} nodes")
        graph = generate_random_graph(n, edge_prob)

        # greedy tests
        start_greedy = time.time()
        greedy_path = find_hamiltonian_path_greedy(graph)
        end_greedy = time.time()
        greedy_time = end_greedy - start_greedy
        greedy_success = "yes" if greedy_path else "no"

        # brute force tests
        start_bf = time.time()
        has_path_bf, bf_path = has_hamiltonian_path_bruteforce(graph)
        end_bf = time.time()
        bf_time = end_bf - start_bf
        bf_success = "yes" if has_path_bf else "no"

        print(f"greedy: {greedy_success} in {greedy_time:.6f}s")
        print(f"bruteforce: {bf_success} in {bf_time:.6f}s")

        node_counts.append(n)
        greedy_times.append(greedy_time)
        brute_times.append(bf_time)

        # save to file
        f.write(f"{n}\t{greedy_time:.6f}\t{bf_time:.6f}\t{greedy_success}\t{bf_success}\n")
        f.flush()

        # timeout
        if bf_time > max_seconds:
            print(f"bruteforce exceeded {max_seconds} seconds at n={n}.")
            break

        n += 1

# plot results
plt.figure(figsize=(10, 6))
plt.plot(node_counts, greedy_times, label='Greedy', marker='o')
plt.plot(node_counts, brute_times, label='Bruteforce', marker='x')
plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.title('Greedy vs Brute-force Hamiltonian Path')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
