import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}




def dijkstra(start,graph):
    Distances= {vertex:float('inf') for vertex in graph}
    visited = {vertex:False for vertex in graph}
    Distances[start] = 0 
    priority_queue = [(0,start)]                        

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if visited[current_vertex] == False:
            visited[current_vertex] = True 
        
            
            
            for neighbor_vertex, weight in graph[current_vertex].items():
                distance = current_distance + weight 

                if distance < Distances[neighbor_vertex] :
                    Distances[neighbor_vertex] = distance 
                    heapq.heappush(priority_queue,(distance,neighbor_vertex))


    return Distances




ShortestPath = dijkstra('A',graph)
print(ShortestPath)
