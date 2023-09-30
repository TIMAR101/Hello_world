""">>> string = "abracadabra"
l = list(string)
 l[5] = 'k'
>string = ''.join(l)
print string
abrackdabra
string = string[:5] + "k" + string[6:]
 print string
abrackdabra"""

def mutate_string(string, position, character):
    lList = list(string)
    lList[position] = character
    result = ''.join(lList)

    return result

def mutate_string1(string, position, character):
    result = string[: position] + character + string[position+1:]

    return result

print(mutate_string("Timofey", 3, "T"))

print(mutate_string1("Timofey", 3, "T"))




