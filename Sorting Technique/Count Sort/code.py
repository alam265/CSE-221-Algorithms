def CountSort(arr):
    max_elem = max(arr)

    count_arr = [0]*(max_elem+1)

    for i in arr:
        count_arr[i]+=1 

    j=k=0 
    while j < len(count_arr):
        if count_arr[j] > 0:
            arr[k]=j 
            count_arr[j]-=1 
            k+=1 
        else:
            j+=1 


arr = [34,5,6,23,67,8,4,34,7,8,34]
CountSort(arr)
print(arr)