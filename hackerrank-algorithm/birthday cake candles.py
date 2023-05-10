def birthdayCakeCandles(candles):
    # Write your code here
    c=0
    temp=candles[0]
    for i in range(1,len(candles)):
        if candles[i]> temp:
            temp=candles[i]
    for i in range(0,len(candles)):
        if candles[i]==temp:
            c=c+1
    return c