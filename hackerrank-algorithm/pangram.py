def pangrams(s):
    count=0
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for leter in alphabet:
        if leter in s.lower():
            count +=0
        else:
            count +=1
    if count ==0:
        return('pangram')
    elif count >0:
        return ('not pangram')