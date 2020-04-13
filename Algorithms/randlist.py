from random import randint

"""
Generate a list of random integers.

"""
def randlist(lower: int, upper: int, size: int) -> list:
    return [randint(lower, upper) for _ in range(size)]
