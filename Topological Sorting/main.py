graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
        4: []
    }

visited = [0]*(len(graph))
topological_list =[]

def DFS():
    for i in range(len(graph)):
        if visited[i] == 0:
            DFS_visit(i)

def DFS_visit(u):
    print(u,end=' ')
    visited[u] = 1 
    for v in graph[u]:
        if visited[v]==0 :
            DFS_visit(v)
    topological_list.insert(0,u)



DFS()
print()
print(topological_list)