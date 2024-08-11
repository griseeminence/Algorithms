class InsertionSort:
    """
    Best case: O(n) - when the array is already sorted.
    Average and worst cases: O(n^2) - when the array is sorted in reverse order.
    """

    @staticmethod
    def sort(arr):

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    InsertionSort.sort(array)
    print("Sorted array:", array)
