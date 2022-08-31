def binSearch(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binSearch(arr, low, mid - 1, x)
        else:
            return binSearch(arr, mid + 1, high, x)
    else:
        return -1
 
arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binSearch(arr, 0, len(arr)-1, x)
 
print(result)