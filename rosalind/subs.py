def subs(str1, str2):
    loc = []
    for i in range(len(str1)):
        if str2 == str1[i: i+len(str2)]:
            loc.append(i+1)
    return loc

if __name__ == "__main__":
    with open("C:/Users/setareh/Documents/rosalind/rosalind_subs.txt", 'r') as f:
        str1 = f.readline().strip()
        str2 = f.readline().strip()
    loc = subs(str1, str2)
    for i in loc:
        print(i, end=" ")