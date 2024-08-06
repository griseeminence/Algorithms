def counter(people: int, tik: int) -> int:
    leader_idx: int = 0
    people_amount: list = list(range(1, people + 1))
    while len(people_amount) > 1:
        leader_idx = (leader_idx - 1 + tik) % len(people_amount)
        del people_amount[leader_idx]
    return people_amount[0]


if __name__ == "__main__":
    people, tik = int(input()), int(input())
    print(counter(people, tik))
