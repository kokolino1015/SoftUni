num = float(input())
s = ""

if num > 0:
    s = "positive"
    if 1 > num > 0:
        print(f"small {s}")
    elif 1000000 > num > 1:
        print(s)
    else:
        print(f"large {s}")
elif num < 0:
    s = "negative"
    if -1 < num < 0:
        print(f"small {s}")
    elif -1000000 < num < -1:
        print(s)
    else:
        print(f"large {s}")
elif num == 0:
    s = "zero"
    print(s)
