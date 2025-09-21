def merge(arr1,arr2):
    res= []
    i=j=0 
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i+=1 
        elif arr1[i] > arr2[j]:
            res.append(arr2[j])
            j+=1 
    while i < len(arr1):
        res.append(arr1[i])
        i+=1
    while j < len(arr2):
        res.append(arr2[j])
        j+=1
    
    return res 

def MergeSort(arr):
    if len(arr)==1:
        return arr 
    else:
        mid = len(arr)//2 
        a1 = MergeSort(arr[:mid])
        a2 = MergeSort(arr[mid:])
        return merge(a1,a2)

Merged_Arr = MergeSort([34,23,45,67,34,24,6,8,5,2])
print(Merged_Arr)

