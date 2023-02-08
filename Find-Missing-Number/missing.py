def findMissingNumbers(n):
    numbers = set(n)
    sorted_list = sorted(list(numbers))
    print(sorted_list)

    first = sorted_list[0]
    last = sorted_list[-1]
    output = []

    for i in range(first, last):
        if i not in sorted_list:
            output.append(i)
    return (output)


listOfNumbers = [-1, -7, 14, 2, -1, -1, 8, 12, 2]
print(findMissingNumbers(listOfNumbers))
