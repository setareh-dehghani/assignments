def dnastrand(string):
    std = ""
    for i in string[::-1]:
        if i == "A":
            std += "T"
        if i == "T":
            std += "A"
        if i == "C":
            std += "G"
        if i == "G":
            std += "C"
    return std


if __name__ == "__main__":
    with open("C:/Users/setareh/Documents/rosalind/rosalind_revc.txt", "r") as f:
        string = f.readline().strip()
        strand = dnastrand(string)
        print(strand)