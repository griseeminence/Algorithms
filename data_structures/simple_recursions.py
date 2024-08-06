class Factorials:

    @staticmethod
    def factorial_recursive(data):
        if data == 0:
            return 1
        else:
            return data * Factorials.factorial_recursive(data - 1)

    @staticmethod
    def factorial_iterative(data):
        result = 1
        for i in range(1, data + 1):
            result *= i
        return result


class Fibonacci:

    @staticmethod
    def fib_recursive(data):
        if data == 0:
            return 0
        elif data == 1:
            return 1
        else:
            return Fibonacci.fib_recursive(data - 1) + Fibonacci.fib_recursive(data - 2)

    @staticmethod
    def fib_recursive_0n(n):
        # Linear Time - On
        if n == 0:
            return 0
        elif n == 1:
            return 1
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]

    @staticmethod
    def fib_iterative(data):
        if data == 0:
            return 0
        elif data == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, data + 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    # Examples
    print('Factorials:')
    print(Factorials.factorial_recursive(5))
    print(Factorials.factorial_iterative(5))
    print('Fibonacci:')
    print(Fibonacci.fib_recursive(10))
    print(Fibonacci.fib_recursive_0n(10))
    print(Fibonacci.fib_iterative(10))
