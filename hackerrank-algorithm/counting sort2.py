def countingSort(arr):
    count = [0]*(max(arr)+1)
    for i in arr:
        count[i]+=1
    sortarr =[]
    for n in range(len(count)):
        while count[n] !=0:
            count[n]-=1
            sortarr.append(n)
    return sortarr