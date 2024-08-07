class LinearSearch:
    """Time complexity is O(n)"""

    def __init__(self, data):
        self.data = data

    def search(self, number):
        for i in range(len(self.data)):
            if self.data[i] == number:
                return i
        return -1



# Example
if __name__ == '__main__':
    ls = LinearSearch([1, 2, 3, 4, 5, 6, 7, 8, 9])
    result = ls.search(5)
    print(result)

    result = ls.search(10)
    print(result)
