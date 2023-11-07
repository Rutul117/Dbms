from collections import deque

def dfs(graph, start):
    visited = set()  # Keep track of visited nodes
    stack = [start]  # Use a stack for DFS

    print("DFS Traversal:")
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Push unvisited neighbors onto the stack in reverse order.
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

# Input: Enter nodes and their neighbors
graph = {}
while True:
    node = input("Enter a node (or press Enter to finish): ")
    if not node:
        break
    neighbors = input(f"Enter neighbors for node {node} (space-separated): ").split()
    graph[node] = neighbors

# Input: Enter the start node for DFS
start_node = input("Enter the start node for DFS: ")

if start_node in graph:
    dfs(graph, start_node)
else:
    print("Start node not found in the graph.")
