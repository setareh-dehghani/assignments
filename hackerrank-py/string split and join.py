def split_and_join(line):
    words = line.split(" ")
    hyphenated = "-".join(words)
    
    return hyphenated
input_str = input()
result = split_and_join(input_str)
print(result)
