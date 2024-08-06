def max_blocks(arr):
    """
    Return the maximum number of blocks for sorting in given array.

    :param arr: List of integers.
    :return: Integer number of blocks.
    """
    n = len(arr)
    if n == 0:
        return 0

    max_val = 0
    blocks = 0

    for i in range(n):
        max_val = max(max_val, arr[i])
        if max_val == i:
            blocks += 1

    return blocks


if __name__ == '__main__':
    nmax = int(input())
    arr = list(map(int, input().split()))[:nmax]
    print(max_blocks(arr))
