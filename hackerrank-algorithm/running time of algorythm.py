def runningTime(arr):
    shifts=0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]>arr[j]):
                shifts +=1
            else:
                shifts=shifts
    return(shifts)