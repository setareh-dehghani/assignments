def dnatorna(string):
    return string.replace('T','U')

if __name__ == "__main__":
    with open("C:/Users/setareh/Documents/rosalind/rosalind_rna.txt", 'r') as f:
        string = f.readline().strip()
        rst = dnatorna(string)
        print(rst)