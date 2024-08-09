class SelectionSort:

    @staticmethod
    def sort(arr):
        """Time complexity is O(n^2)"""
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


# Example
array = [64, 25, 12, 22, 11]
sorted_array = SelectionSort.sort(array)
print("Sorted array:", sorted_array)
