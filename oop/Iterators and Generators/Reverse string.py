def reverse_text(num):
    start = len(num) - 1
    while start > -1:
        yield num[start]
        start -= 1
