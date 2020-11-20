n = int(input())
word = input()
list_all = []
list_w = []
for i in range(1, n + 1):
    s = input()
    list_all.append(s)
    if word in s:
        list_w.append(s)
print(list_all)
print(list_w)