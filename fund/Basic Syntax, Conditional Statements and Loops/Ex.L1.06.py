year = int(input())

while True:
    year += 1
    g = str(year)
    if len(set(g)) == len(g):
        print(year)
        break
