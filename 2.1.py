lis = []
with open("2.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        lis.append(line)
horizontal = 0
vertical = 0
for entry in lis:
    if "forward" in entry:
        horizontal += int(entry[-1])
    elif "down" in entry:
        vertical += int(entry[-1])
    if "up" in entry:
        vertical -= int(entry[-1])

print(horizontal*vertical)

