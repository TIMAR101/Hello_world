def count_substring(string, sub_string):

    count = 0
    lenst = len(string)
    lensub = len(sub_string)

    for item in range(lenst):

        if string[item:item + lensub] == sub_string:
            count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


