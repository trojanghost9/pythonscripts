# used to yield the result of adding numbers from a list


def add():
    # list = [1, 2, 3, 4, 5, 6]
    # for x in list:
    #     sum = x + 1
    #     yield sum
    for x in range(10,100000):
        result = x * 42
        yield result
