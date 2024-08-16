class Solution:

    @staticmethod
    def remove_duplicates(nums: list[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1


if __name__ == "__main__":
    # Example
    example1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    example2 = [1, 1, 2]
    print(Solution.remove_duplicates(example1))
    print(Solution.remove_duplicates(example2))