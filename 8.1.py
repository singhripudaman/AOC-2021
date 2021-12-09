import re
pattern = re.compile(r'[A-Z a-z]+ \| ([A-Z a-z]+)')
lis = []
with open("8.txt", "r") as f:
    for line in f:
        match = pattern.match(line)
        lis.append(match.group(1))
count = 0

individual = [element.split() for element in lis]
for element in individual:
    for word in element:
        if (len(word) == 2) or (len(word) == 4) or (len(word) == 3) or (len(word) == 7):
            count += 1
print(count)
