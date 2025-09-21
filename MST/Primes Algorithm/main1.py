import heapq 
graph = {                                       # This graph is taken from Striver's Video 
    "A": [(2, "B"), (1, "C")], 
    "B": [(2, "A"), (1, "C")], 
    "C": [(1, "A"), (1, "B"), (2, "E"), (2, "D")], 
    "D": [(2, "C"), (1, "E")], 
    "E": [(2, "C"), (1, "D")] 
}

visited = {v:False for v in graph} 
 

pq = [(0, "A", "-1")]  

mst = []
cost = 0

heapq.heapify(pq) 


while pq: 
    w, nbr, parent = heapq.heappop(pq) 
    if visited[nbr] == False:
        visited[nbr] = True 
        mst.append((parent, nbr)) 
        cost += w 

        for elem in graph[nbr]: 
            w = elem[0] 
            nbr1 = elem[1] 

            if visited[nbr1] == False: 
                heapq.heappush(pq, (w, nbr1, nbr)) 



print(mst[1:] , cost)