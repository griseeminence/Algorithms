def decrypt(arr):
    """
    Function decrypts the given string using the given multiplier.

    :param arr: string with sequence of integers, characters and brackets.
    :return: decrypted string with sequence of characters (depends on multiplier) in sequence.
    """
    stack: list = []
    result: str = ""
    multiplier: int = 0

    for char in arr:
        if char.isdigit():
            multiplier = multiplier * 10 + int(char)
        elif char == '[':
            stack.append((result, multiplier))
            result, multiplier = "", 0
        elif char == ']':
            prev_result, prev_multiplier = stack.pop()
            result = prev_result + prev_multiplier * result
        else:
            result += char

    return result


if __name__ == '__main__':
    arr: str = input()
    print(decrypt(arr))