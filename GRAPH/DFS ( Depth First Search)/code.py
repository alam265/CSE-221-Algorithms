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


def DFS(firt_vrtx):
    global flag 
    if visited[firt_vrtx] == 0:
        print(firt_vrtx,end=' ')
        visited[firt_vrtx] = 1 
        for i in range(1,V+1):
            if A[firt_vrtx][i] == 1 and visited[i]==0:
                DFS(i)
DFS(1)
