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

# test runs
max_seconds = 2
edge_prob = 0.5
n = 2
node_counts = []
greedy_times = []
retry_counts = []

# export results file
with open("results.txt", "w") as f:
    f.write("node_number\tgreedy_time\tretry_count\tgreedy_path\n")

    while True:
        print(f"\n{n} nodes")

        retry_count = 1
        greedy_path = None
        start_greedy = time.time()

        while greedy_path is None:
            graph = generate_random_graph(n, edge_prob)
            greedy_path = find_hamiltonian_path_greedy(graph)
            if greedy_path is None:
                retry_count += 1

        end_greedy = time.time()
        greedy_time = end_greedy - start_greedy

        print(f"greedy: success in {greedy_time:.6f}s after {retry_count} attempt(s)")

        node_counts.append(n)
        greedy_times.append(greedy_time)
        retry_counts.append(retry_count)

        # save to file
        f.write(f"{n}\t{greedy_time:.6f}\t{retry_count}\tyes\n")
        f.flush()

        # break only if slow on first try
        if greedy_time > max_seconds and retry_count == 1:
            print(f"Terminated: greedy_time > {max_seconds} on first attempt (n={n})")
            break

        n += 1

# plot results
plt.figure(figsize=(10, 6))
plt.plot(node_counts, greedy_times, label='Greedy', marker='o')
plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.title('Greedy Hamiltonian Path')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
