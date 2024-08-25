class Solution:
    @staticmethod
    def profit(prices):
        left_idx = 0
        right_idx = 1
        max_profit = 0
        while right_idx < len(prices):
            profit = prices[right_idx] - prices[left_idx]
            if prices[left_idx] < prices[right_idx]:
                max_profit = max(max_profit, profit)
            else:
                left_idx = right_idx
            right_idx += 1
        return max_profit


if __name__ == '__main__':
    # Examples
    prices_1 = [7, 1, 5, 3, 6, 4]
    print(f'Max profit: {Solution.profit(prices_1)}')
    prices_2 = [7, 6, 4, 3, 1]
    print(f'Max profit:: {Solution.profit(prices_2)}')
