def closestNumbers(arr):
    output=[]
    arr=sorted(arr)
    nowmin=10**9
    for inx in range(1,len(arr)):
        diff=abs(arr[inx-1]-arr[inx])
        
        if diff <nowmin:
            output=[(arr[inx-1],arr[inx])]
            nowmin=diff
        elif diff == nowmin:
            output.append((arr[inx-1],arr[inx]))
    flat_list=[item for sublist in output for item in sublist]
    return flat_list