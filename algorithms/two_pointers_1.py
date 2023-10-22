# Код посылки на Яндекс.Контест: 94078403

def dostavka(data: list[int], limit: int) -> int:
    """
    Calculating the required number of platforms for cargo delivery.

    :param data: A list of integers representing the weight of each item.
    :param limit: An integer representing the maximum weight capacity of a platform.
    :return: The number of platforms required to deliver the entire volume of cargo.
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
    data: list[int] = [int(i) for i in input().split(' ')]
    limit: int = int(input())
    print(dostavka(data, limit))
