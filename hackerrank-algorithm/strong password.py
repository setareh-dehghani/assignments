def minimumNumber(n, password):
    numbers="0123456789"
    lower_case="abcdefghijklmnopqrstuvwxyz"
    upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special="!@#%^&*()+=-"
    count=0
    if any(i.isdigit() for i in password)==False:
        count +=1
    if any(i.islower() for i in password)==False:
        count +=1
    if any(i.isupper()for i in password) == False:
        count +=1
    if any(i in special for i in password)==False:
        count +=1
    return max(count,6-n)