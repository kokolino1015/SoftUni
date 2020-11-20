n = int(input())
pos = 0
pos_list = []
neg = 0
neg_list = []

for i in range(1, n + 1):
    s = int(input())
    if s > 0:
        pos += 1
        pos_list.append(s)
    elif s < 0:
        neg += s
        neg_list.append(s)

print(pos_list)
print(neg_list)
print(f"Count of positives: {pos}. Sum of negatives: {neg}")