def max_subArray_sum(arr,low, high):
    if low == high:
        return arr[low]
    mid = (low + high)//2
    left_max = max_subArray_sum(arr, low, mid)
    right_max = max_subArray_sum(arr, mid+1,high)

    left_cross_sum = float('-inf')
    current_sum = 0 
    for i in range(mid, low-1 ,-1):
        current_sum+= arr[i]
        if current_sum > left_cross_sum:
            left_cross_sum = current_sum 

    right_cross_sum = float('-inf')
    current_sum = 0 
    for j in range(mid+1 , high+1):
        current_sum += arr[j]
        if current_sum > right_cross_sum:
            right_cross_sum = current_sum 

    cross_sum = left_cross_sum + right_cross_sum 

    return max(left_max, right_max, cross_sum)

max_value = max_subArray_sum([-2,1,-3,4,-1,2,1,-5,4],0, 8)

print(max_value)

