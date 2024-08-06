def index_determination(massive: list, target: int) -> int:
    """
    Поиск индекса элемента в массиве.
    Возвращает индекс элемента в массиве, если он содержится в массиве.
    Возвращает возможный индекс, если элемент не содержится в массиве.
    """
    left = 0
    right = len(massive) - 1
    while left <= right:
        mid = (left + right) // 2
        if massive[mid] == target:
            right = mid
            right -= 1
        elif massive[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    massive = [int(x) for x in input().split()]
    target = int(input())
    print(index_determination(massive, target))
