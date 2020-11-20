peoples = int(input())
all_peoples = peoples
lifts = input().split(" ")
lifts = [int(x) for x in lifts]
passions = 0

for i in lifts:
    passions += i

for i in range(len(lifts)):
    if lifts[i] == 4:
        continue
    if peoples == 0:
        break
    while True:
        if peoples == 0:
            break
        if lifts[i] == 4:
            break
        lifts[i] += 1
        peoples -= 1

if peoples == 0:
    if (len(lifts) * 4) - passions == all_peoples:
        lifts = [str(x) for x in lifts]
        print(" ".join(lifts))
    else:
        print("The lift has empty spots!")
        lifts = [str(x) for x in lifts]
        print(" ".join(lifts))
else:
    print(f"There isn't enough space! {peoples} people in a queue!")
    lifts = [str(x) for x in lifts]
    print(" ".join(lifts))
