class BubbleSort:
    """Time complexity is O(n^2)"""

    @staticmethod
    def sort(arr):

        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = BubbleSort.sort(array)
    print("Sorted array:", sorted_array)
