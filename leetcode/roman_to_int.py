class Solution:

    @staticmethod
    def roman_to_int(s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        for char in s:
            current_value = roman_values[char]

            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value

        return total


if __name__ == '__main__':
    # Example
    example1 = 'III'
    example2 = 'LVIII'
    example3 = 'MCMXCIV'

    solution = Solution()
    print(solution.roman_to_int(example1))
    print(solution.roman_to_int(example2))
    print(solution.roman_to_int(example3))
