def two_sum(nums: list, target: int):
    """
    This function iterates through the array once, so it has a time complexity of O(n),
    where n is the number of elements in the array. The space complexity is also O(n)
    due to the use of the dictionary to store the complements. (!) Only one successful case.
    """
    result_dict = {}
    for i, y in enumerate(nums):
        complement: int = target - y
        if complement in result_dict:
            return [result_dict[complement], i]
        result_dict[y] = i
    return []
