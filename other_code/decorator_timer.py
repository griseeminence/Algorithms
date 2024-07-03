import time


def timer(func):
    """
    Basic timer decorator.
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Function duration: {(end - start):.2f} seconds')
        return result

    return wrapper

#check
@timer
def example_multiplication_table(size: int) -> list:
    """
    Example of multiplication table.
    """
    time.sleep(1)
    table = [
        [i * j for j in range(1, size + 1)]
        for i in range(1, size + 1)
    ]
    return table


if __name__ == '__main__':
    table_size: int = int(input())
    example_multiplication_table(table_size)
