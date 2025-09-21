def InsertionSort(arr):
    for i in range(1,len(arr)):
        j = i-1 
        x = arr[i]
        while j>-1 and x < arr[j]:
            arr[j+1] = arr[j]
            j-=1 
        arr[j+1] = x 


arr =[8,5,7,3,2]

InsertionSort(arr)

print(arr)