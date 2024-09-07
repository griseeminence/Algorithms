class QuickSort:
    """Time complexity is O(log'n)"""

    @staticmethod
    def sort(arr, low, high):
        if low < high:
            pivot_idx = QuickSort.partition(arr, low, high)
            QuickSort.sort(arr, low, pivot_idx - 1)
            QuickSort.sort(arr, pivot_idx + 1, high)

    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


if __name__ == "__main__":
    array_1 = [5, 4, 3, 2, 1]
    QuickSort.sort(array_1, 0, len(array_1) - 1)
    print(array_1)
