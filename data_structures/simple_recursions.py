class Factorials:

    def __init__(self, data):
        self.data = data

    def factorial_rec(self, data=None):
        if data is None:
            data = self.data
        if data == 0:
            return 1
        else:
            return data * self.factorial_rec(data - 1)

    def factorial_base(self, data=None):
        if data is None:
            data = self.data
        result = 1
        for i in range(1, data + 1):
            result *= i
        return result


if __name__ == '__main__':
    # Example
    n = Factorials(5)
    print("Factorial (recursive):", n.factorial_rec())
    print("Factorial (iterative):", n.factorial_base())
