class Solution:
    @staticmethod
    def is_palindrome(s):
        result = ''.join([i.lower() for i in s if i.isalnum()])
        return result == result[::-1]


if __name__ == '__main__':
    # Example
    s = 'A man, a plan, a canal: Panama'
    print(Solution.is_palindrome(s))
