def template_sort(arr: list[int], template: list[int]) -> str:
    """
    Sorts arr according to the template.
    """
    dictionary_container: dict = {}
    for container in arr:
        if container in dictionary_container:
            dictionary_container[container].append(container)
        else:
            dictionary_container[container] = [container]

    result: list = []
    for j in template:
        if j in dictionary_container:
            result.extend(dictionary_container[j])
            del dictionary_container[j]

    not_in_template: list = []
    for remainder in dictionary_container.keys():
        not_in_template.extend(dictionary_container[remainder])

    result.extend(sorted(not_in_template))
    return ' '.join(map(str, result))

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    m = int(input())
    template = list(map(int, input().split()))[:m]
    print(template_sort(arr, template))