class MergeSort:
    """Time complexity is O(log'n)"""

    @staticmethod
    def sort(arr):
        """Sorts the array using merge sort algorithm."""
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = MergeSort.sort(arr[:mid])
        right_half = MergeSort.sort(arr[mid:])

        return MergeSort.merge(left_half, right_half)

    @staticmethod
    def merge(left, right):
        """Merges two sorted arrays into one sorted array."""
        sorted_array = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                sorted_array.append(left[left_index])
                left_index += 1
            else:
                sorted_array.append(right[right_index])
                right_index += 1

        sorted_array.extend(left[left_index:])
        sorted_array.extend(right[right_index:])

        return sorted_array


# Example
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    sorted_array = MergeSort.sort(array)
    print("Sorted array:", sorted_array)
