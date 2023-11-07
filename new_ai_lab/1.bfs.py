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

def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Use a queue for BFS
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Start BFS from node 'A'
print("BFS Traversal:")
bfs(graph, 'A')
