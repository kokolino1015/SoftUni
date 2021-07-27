def fibonacci():
    result = [0, 1, 1]
    yield 0
    yield 1
    yield 1
    index = 2
    while True:
        n = result[index] + result[index-1]
        yield n
        result.append(n)
        index += 1
