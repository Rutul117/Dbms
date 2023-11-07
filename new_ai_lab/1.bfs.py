from collections import deque

def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Use a queue for BFS
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Input: Enter nodes and their neighbors
graph = {}
while True:
    node = input("Enter a node (or press Enter to finish): ")
    if not node:
        break
    neighbors = input(f"Enter neighbors for node {node} (space-separated): ").split()
    graph[node] = neighbors

# Start BFS from a node
start_node = input("Enter the start node for BFS: ")

if start_node in graph:
    print("BFS Traversal:")
    bfs(graph, start_node)
else:
    print("Start node not found in the graph.")
