from queue import Queue

q = Queue()

V = 7 
A = [[0,0,0,0,0,0,0,0],
     [0,0,1,1,1,0,0,0],
     [0,1,0,1,0,0,0,0],
     [0,1,1,0,1,1,0,0],
     [0,1,0,1,0,1,0,0],
     [0,0,0,1,1,0,1,1],
     [0,0,0,0,0,1,0,0],
     [0,0,0,0,0,1,0,0],  
     
     ]
visited = [0]*(V+1)
parent = [0]*(V+1)

def BFS(firs_vrtx):
    

    
    print(firs_vrtx, end=' ')
    visited[firs_vrtx] = 1 
    q.enqueue(firs_vrtx)

    while not q.isEmpty():
        u = q.dequeue()
        for v in range(1,V+1):
            if A[u][v] == 1 and visited[v] == 0:
                print(v,end=' ')
                visited[v] = 1 
                parent[v] = u 
                q.enqueue(v)


BFS(1)

print()


# Shortest Path using BFS
source =1
destination_node = 7 
while destination_node !=source:
    print(destination_node)
    destination_node = parent[destination_node]


print(source)
    








