class QuickSort:
    """Time complexity is O(log'n)"""

    @staticmethod
    def sort(arr):
        if len(arr) <= 1:
            return arr

        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return QuickSort.sort(left) + middle + QuickSort.sort(right)


# Пример использования
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    sorted_array = QuickSort.sort(array)
    print("Sorted array:", sorted_array)
