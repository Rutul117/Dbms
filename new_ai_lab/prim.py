DFS bfs

graph = {
    1: [4, 7, 9],
    2: [5, 6,7],
    3: [4,9],
    4: [1,3,6,8],
    5: [2,9],
    6: [2,4],
    7: [1,2],
    8: [4],
    9: [1,3,5]
}
visted_dfs =[]
visted_bfs =[]
queue = []



def dfs(graph,visted_dfs,node):
    if node not in visted_dfs:
        visted_dfs.append(node)
        print(node, end=' ')
        for n in graph[node]:
            dfs(graph,visted_dfs,n)

def helperrecursion(visted_dfs, queue):
    if not queue:
        return
    m = queue.pop(0)
    print(m,end=' ')
    for n in graph[m]:
        if n not in visted_dfs:
            visted_dfs.append(n)
            queue.append(n)
    helperrecursion(visted_dfs,queue)
def bfs(visted_dfs,queue,node):
    visted_dfs.append(node)
    queue.append(node)
    helperrecursion(visted_dfs,queue)
print("this is bfs algo")
bfs(visted_dfs,queue,1)
print("\nthis is dfs algo")
dfs(graph,visted_bfs,1)