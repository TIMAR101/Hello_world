def most_common(s):
    # Create dictionary with each letter and their frequency
    d = {}
    for char in s:
        d[char] = d.get(char, 0) + 1

    # Get sorted keys (sort largest to smallest + alphabetical)
    sorted_keys = sorted(d, key=lambda x: (-d[x], x))

    for i in range(3):
        print(sorted_keys[i], d[sorted_keys[i]])

f=lambda x: (-d[x], x)

d = {"a": 5, "c": 2}

print(f)

print(f("a"))
