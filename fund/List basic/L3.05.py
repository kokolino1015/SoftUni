n = int(input())
s = []
f = []
for i in range(1, n + 1):
    num = int(input())
    s.append(num)
command = input()

if command == "positive":
    for g in s:
        if g == 0:
            f.append(g)
        if g > 0:
            f.append(g)
elif command == "negative":
    for g in s:
        if g == 0:
            continue
        if g < 0:
            f.append(g)
elif command == "even":
    for g in s:
        if g % 2 == 0:
            f.append(g)
elif command == "odd":
    for g in s:
        if g % 2 != 0:
            f.append(g)

print(f)