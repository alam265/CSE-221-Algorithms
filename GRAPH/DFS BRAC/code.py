"""
This Algo will work for both Directed and Undirected Graph
"""


V = 7 
A = [[0,0,0,0,0,0,0,0],   #0
     [0,0,1,0,1,0,0,0],   #1
     [0,0,0,1,0,0,0,0],   #2
     [0,1,0,0,0,1,0,0],   #3
     [0,0,0,1,0,1,0,0],   #4
     [0,0,0,0,0,0,0,1],   #5
     [0,0,0,0,0,1,0,0],   #6
     [0,0,0,0,0,0,0,0],   #7
     
     ]
color = ['white']*(V+1)  
time = 0 
start_time=[0]*(V+1)
finish_time=[0]*(V+1)


def DFS():
    for v in range(1,len(A)):
        if color[v] == 'white':
            DFS_visit(v)

def DFS_visit(u):
    global time 
    print(u,end=' ')
    color[u] = 'grey'
    time+=1 
    start_time[u] = time 

    for v  in range(1,V+1):
        if A[u][v] == 1 and color[v] == 'white':
            DFS_visit(v)
    color[u] = 'black'
    time+=1 
    finish_time[u] = time 


DFS()
print()
print(finish_time[1:])



