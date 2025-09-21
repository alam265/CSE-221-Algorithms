def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]
   
    # Initialize the index of the smaller element
    i = low - 1
   
    # Iterate through the array from low to high-1
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            # Swap arr[i+1] and arr[j]
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Swap the pivot (arr[high]) with the element at the partition index (arr[i+1])
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
   
    # Return the partition index
    return i + 1
def quicksort(arr, low, high):
    if low <= high:
        # Partition the array
        pivot_index = partition(arr, low, high)
       
        # Recursively sort the left and right subarrays
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)



arr =[1,3,5,7,4,3,5,78,452,356,78]
quicksort(arr,0,len(arr)-1)
print(arr)