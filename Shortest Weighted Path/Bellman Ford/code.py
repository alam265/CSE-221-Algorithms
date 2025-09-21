graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {'B': -10}
}

def bellman_ford(graph,st_v):
    Distances = {vertex:float('inf') for vertex in graph}
    Distances[st_v] = 0 

    for _ in range(len(graph)-1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                distance = Distances[vertex] + weight 
                if distance < Distances[neighbor]: 
                    Distances[neighbor] = distance 




    # Detecting Negative weight cycle 
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            distance = Distances[vertex] + weight 
            if distance < Distances[neighbor]: 
                return "Negative Weight cycle exist. Graph can not be solved"
                
            
    return Distances












start_vertex = 'A'
result = bellman_ford(graph, start_vertex)
print(result)
