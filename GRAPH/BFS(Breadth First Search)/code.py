from queue import Queue

q = Queue()

vertices = 7 
matrix = [[0,0,0,0,0,0,0,0],
     [0,0,1,1,1,0,0,0],
     [0,1,0,1,0,0,0,0],
     [0,1,1,0,1,1,0,0],
     [0,1,0,1,0,1,0,0],
     [0,0,0,1,1,0,1,1],
     [0,0,0,0,0,1,0,0],
     [0,0,0,0,0,1,0,0],  
     
     ]


visited = [0]*(vertices+1)
parent = [0]*(vertices+1)
distance = [0]*(vertices+1)

def BFS(firs_vrtx):

    print(firs_vrtx,end=' ')
    visited[firs_vrtx] = 1 
    distance[firs_vrtx] = 0
    q.enqueue(firs_vrtx)

    while not q.isEmpty():
        u = q.dequeue()
        for v in range(1,vertices+1):         
            if matrix[u][v] ==1 and visited[v] == 0:
                
                
                visited[v] = 1 
                parent[v] = u
                distance[v] = distance[u]+1

                print(v,end=' ')
                
                q.enqueue(v)


BFS(1)








