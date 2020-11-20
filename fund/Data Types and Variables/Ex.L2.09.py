n = int(input())
max_v = -999999999
max_s = 0
max_t = 0
max_q = 0

for i in range(1, n + 1):
    snow = int(input())
    time = int(input())
    quality = int(input())
    v = snow // time
    value = v ** quality
    if value > max_v:
        max_v = value
        max_s = snow
        max_t = time
        max_q = quality

print(f"{max_s} : {max_t} = {max_v} ({max_q})")
