import re
with open('text.txt') as file:
    text = file.read().split('-')
text.pop(0)
index = 0
for i in text:
    if index % 2 == 0:
        i = re.sub('[-.,?!]', '@', i)
        line = ' '.join(reversed(i.split()))
        print(line)
    index += 1
