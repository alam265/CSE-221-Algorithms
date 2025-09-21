graph = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [4],
        4: [3]
 }

def transpose_graph():
    trans_graph = {}
    for i in range(len(graph)):
        trans_graph[i] =[]

    for k,v in graph.items():
        for i in v:
            trans_graph[i].append(k)
    return trans_graph
        

def DFS_visit(u,visited,stack):
    visited[u] = 1

    for v in graph[u]:
        if visited[v] == 0:
            DFS_visit(v,visited,stack)
    stack.append(u)

def DFS_SCC(u,scc,visited,transposed_Graph):
    visited[u] = 1
    scc.append(u)

    for v in transposed_Graph[u]:
        if visited[v] == 0:
            DFS_SCC(v,scc,visited,transposed_Graph)

    


def strongly_connected_components():
    stack =[]
    visited =[0]*len(graph)
    for u in range(len(graph)):
        if visited[u] == 0:
            DFS_visit(u,visited,stack)


    transposed_Graph = transpose_graph()
    visited = [0]*len(graph) 
    All_scc =[]

    while stack:
        u = stack.pop()
        if visited[u] == 0:
            scc=[]
            DFS_SCC(u,scc,visited,transposed_Graph)
            All_scc.append(scc)

    return All_scc 


result = strongly_connected_components()

print(result)

        


    




