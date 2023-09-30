def split_and_join(line):
    # write your code here
    
    line = line.split(" ")
    print(type(line))
    line = "-".join(line)
    return line


print(split_and_join("Timofey is multi billionare!!!"))
