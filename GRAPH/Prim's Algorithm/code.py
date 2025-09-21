I = float("inf")
V  = 7
# t will be edge. edge = vertices - 1
t = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],    
] 

near = [I]*(V+1)
cost = [
            [I, I, I, I, I, I, I, I],
            [I, I, 25, I, I, I, 5, I],
            [I, 25, I, 12, I, I, I, 10],
            [I, I, 12, I, 8, I, I, I],
            [I, I, I, 8, I, 16, I, 14],
            [I, I, I, I, 16, I, 20, 18],
            [I, 5, I, I, I, 20, I, I],
            [I, I, 10, I, 14, 18, I, I],
]

def Prims_Algorithm():

    min_cost = I 
    v = u = 0
    for row in range(1,V+1):
        near[row]= I
        for col in range(row,V+1):
            if cost[row][col] < min_cost:
                min_cost = cost[row][col]
                u = row 
                v = col 
            
    t[0][0] = u 
    t[1][0] = v 
    near[u] =  near[v] = 0 


    for i in range(1,len(near)):
        if near[i]!=0:
            if cost[i][u] < cost[i][v] :
                near[i] = u 
            else:
                near[i] = v 


    for i in range(1,len(t[0])):
        k=0
        min_cost = I 
        for j in range(1,len(near)):
            if near[j]!=0 and cost[j][near[j]] < min_cost:
                min_cost = cost[j][near[j]]
                k = j 

        t[0][i] = k 
        t[1][i] = near[k] 
        near[k] = 0

        for j in range(1,len(near)):
            if near[j]!=0 and cost[j][k] < cost[j][near[j]] :
                near[j] = k 



def minimum_cost():
    sum = 0
    for i in range(len(t[0])):
        sum += cost[t[0][i]][t[1][i]]
 

    print("Minimum cost: ",sum)



Prims_Algorithm()
print(t)
minimum_cost()