def solution(string):

    List1 = list(string)

    List1.reverse()
    result1 = ''.join(List1)
    result2 = str(List1)
    print(result1)
    print(result2)
    print(type(result2))

    return None

def solution1(string):
    # Pythonic way :)
    return string[::-1]

    # For beginners it's good practise
    # to know how reverse() or [::-1]
    # works on the surface
    #for char in range(len(string)-1,-1,-1):
        #return string[char]

print(solution1("Timofey"))
