import heapq
class DisjointSet:
    def __init__(self, nof_vertices):
        self.n_v = nof_vertices 
        self.parent = [-1] * (self.n_v + 1)

    def find(self, node):
        x = node 
        while self.parent[x] > 0:
            x = self.parent[x]
        return x  

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        
        if self.parent[u] < self.parent[v]:
            self.parent[u] += self.parent[v]
            self.parent[v] = u
        else:
            self.parent[v] += self.parent[u]
            self.parent[u] = v
        

graph ={1: {2: 10, 3: 8, 4: 6}, 
        2: {1: 10, 3: 7, 5: 7}, 
        3: {1: 8, 2: 7, 4: 12}, 
        4: {1: 6, 3: 12, 5: 9}, 
        5: {2: 7, 4: 9}
        }


def Kruskal(graph):
    priority_queue = []    
    for v_f in graph:
        for v_t,weight in graph[v_f].items():
            priority_queue.append((weight,v_f,v_t))


    heapq.heapify(priority_queue)

    dsu = DisjointSet(len(graph)) 
    path =[]
    total_minimum_weight = 0
    while priority_queue:
        w,v_t,v_f = heapq.heappop(priority_queue)
        if dsu.find(v_t) != dsu.find(v_f)  :
            dsu.union(v_t,v_f)
            path.append((v_t,v_f,w)) 
            total_minimum_weight += w 

    return total_minimum_weight



print(Kruskal(graph))
        

