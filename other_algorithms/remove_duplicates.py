def duplicate(massive: list) -> str:
    """
    Удаляет дубликаты из списка.
    Добавляет в конец списка '_' в количестве равно количеству дубликатов.
    Возвращает отсортированную строку элементов списка.
    """
    unique_massive = sorted(list(set(massive)))
    to_extend = len(massive) - len(unique_massive)
    unique_massive.append('_ ' * to_extend)
    return ' '.join(map(str, unique_massive))


if __name__ == '__main__':
    count = int(input())
    massive = [int(x) for x in input().split()][:count]
    print(duplicate(massive))
#check