import itertools

with open("C:/Users/setareh/Documents/rosalind/rosalind_lexf.txt", 'r') as f:
    string = f.readline().split()
    n = int(f.readline().strip())
    result = list(itertools.product(string, repeat = n))
    print("\n".join(["".join(x) for x in result]))