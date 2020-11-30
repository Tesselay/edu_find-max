def findMaxIterative(own_list):

    max_val = own_list[0]
    for i in range(1, len(own_list)):
        if own_list[i] > max_val:
            max_val = own_list[i]

    return max_val


def findMaxRecursive(list):
    # Base case, will go through the list
    if len(list) == 1:
        return list[0]
    else:
        # As long, as there is > 1 elem in the list, another function will be called
        m = findMaxRecursive(list[1:])
        # When arriving at the last elem, the recursive calls will be reversed and the functions continue with the comparison
        return m if m > list[0] else list[0]


if __name__ == '__main__':
    test_list = [19, 32, 25, 5, 67, 23]

    print(findMaxIterative(test_list))
    print(findMaxRecursive(test_list))