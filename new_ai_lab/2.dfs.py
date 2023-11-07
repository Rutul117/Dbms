from collections import deque

# Define a graph using an adjacency list.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

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
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

dfs(graph,'A')