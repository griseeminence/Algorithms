class BinarySearch:

    def __init__(self, arr):
        self.arr = arr

    def iterative_search(self, target):
        left, right = 0, len(self.arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def _recursive_search(self, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if self.arr[mid] == target:
            return mid
        elif self.arr[mid] < target:
            return self._recursive_search(target, mid + 1, right)
        else:
            return self._recursive_search(target, left, mid - 1)

    def recursive_search(self, target):
        return self._recursive_search(target, 0, len(self.arr) - 1)


if __name__ == '__main__':
    # Example:
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    binary_search = BinarySearch(arr)
    iter_result = binary_search.iterative_search(target)
    if iter_result != -1:
        print(f'Iterative search: Element found at index {iter_result}')
    else:
        print('Iterative search: Element not found')
    recur_result = binary_search.recursive_search(target)
    if recur_result != -1:
        print(f'Recursive search: Element found at index {recur_result}')
    else:
        print('Recursive search: Element not found')
