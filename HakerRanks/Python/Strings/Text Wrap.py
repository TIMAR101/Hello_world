import textwrap

def wrap(string, max_width):

    St = textwrap.wrap(string, width=max_width)
    St1 ="\n".join(St)

    return St1

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
