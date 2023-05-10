def insertionSort2(n, arr):
    for i in range(1,n):
        trc=i-1
        count=arr[i]
        while(trc >= 0 and arr[trc]>count):
            arr[trc +1]=arr[trc]
            trc=trc-1
            arr[trc+1]=count
        print(*arr)