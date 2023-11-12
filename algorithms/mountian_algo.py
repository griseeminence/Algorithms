def mountians(array: list) -> bool:
    """
    To find the maximum index in an unsorted array.
    Then check if the array is sorted until maximum index
    and reverse sorted after maximum index.

    :param array: list of integers
    :return: boolean value
    """
    max_index: int = array.index(max(array))
    if len(array) < 3:
        return False
    if max_index == 0 or max_index == len(array) - 1:
        return False
    for i in range(1, max_index):
        if array[i] <= array[i - 1]:
            return False
    for y in range(max_index + 1, len(array)):
        if array[y] >= array[y - 1]:
            return False
    return True


if __name__ == '__main__':
    array = list(map(int, input().split(' ')))
    print(mountians(array))
