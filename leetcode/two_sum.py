class Solution:

    @staticmethod
    def two_sum(nums, target):
        result = {}
        for i, y in enumerate(nums):
            res = target - y
            if res in result:
                return [result[res], i]
            result[y] = i
        return []


if __name__ == "__main__":
    # Example
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution.two_sum(nums, target))
