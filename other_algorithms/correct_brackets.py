def correct_bracket(value: str) -> bool:
    """
    Check whether the bracket query is 'correct' or not.

    :param value: str with the bracket query
    :return: bool value if the bracket query is correct
    """
    stack: list = []
    bracket_dict: dict = {')': '(', '}': '{', ']': '['}
    for i in value:
        if i in bracket_dict.values():
            stack.append(i)
        elif i in bracket_dict:
            if not stack or stack.pop() != bracket_dict[i]:
                return False
    return not stack


if __name__ == '__main__':
    value = input()
    print(correct_bracket(value))
#check