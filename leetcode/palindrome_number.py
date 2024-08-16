class Solution:

    @staticmethod
    def is_palindrome(x: int) -> bool:
        return str(x) == str(x)[::-1]


# Example
if __name__ == '__main__':
    number = 121
    example = Solution.is_palindrome(number)
    print(f'If {number} is polindrome? - {example}')
