# Код посылки на Яндекс.Контест: 94078403

def dostavka(data: list[int], limit: int) -> int:
    """
    Определение необходимого количества платформ для доставки груза.

    :param data: Список целых чисел, представляющих вес товара;
    :param limit: Целое число, представляющее максимальный вес для платформы;
    :return: Количество платформ, необходимое для доставки всего объема товара;
    """
    data.sort()
    left: int = 0
    right: int = len(data) - 1
    platform: int = 0
    while left <= right:
        if data[left] + data[right] <= limit:
            left += 1
        right -= 1
        platform += 1
    return platform


if __name__ == "__main__":
    data: list = [int(i) for i in input().split(' ')]
    limit: int = int(input())
    print(dostavka(data, limit))
