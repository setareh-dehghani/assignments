def marsExploration(s):
    count=0
    for i in range(0,len(s),3):
        SOS=s[i:i+3]
        if SOS[0]!="S":
            count +=1
        if SOS[1]!= "O":
            count +=1
        if SOS[2] != "S":
            count+=1
    return(count)