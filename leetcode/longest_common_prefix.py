class Solution:

    @staticmethod
    def longest_common_prefix(lst: list[str]) -> str:
        if not lst:
            return ""
        lst.sort()
        i = 0
        first, last = lst[0], lst[-1]
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]


if __name__ == "__main__":
    # Example
    example = ["flower", "flow", "flight"]
    solution = Solution.longest_common_prefix(example)
    print(solution)
