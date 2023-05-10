def quickSort(arr):
    right=[]
    left=[]
    equal=[]
    pivot=arr[0]
    
    for e in arr:
        if e<pivot:
            left.append(e)
        else:
            right.append(e)
    return left +right