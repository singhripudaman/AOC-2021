lis = []
with open("10.txt", "r") as f:
    for line in f:
        lis.append(line.rstrip())
chars = {"(":")", "[":"]", "{":"}", "<":">"}
points = {"(":1, "[":2, "{":3, "<":4}
incomplete = []
scores = []
for line in lis:
    illegal = False
    stack = []
    for char in line:
        if char in chars:
            stack.append(char)
        else:
            if char != chars[stack.pop()]:
                illegal = True
        if illegal:
            break
    if not illegal:
        incomplete.append(line)
for line in incomplete:
    score = 0
    stack = []
    for char in line:
        if char in chars:
            stack.append(char)
        else:
            stack.pop()
    stack.reverse()
    for char in stack:
        score *= 5
        score += points[char]
    scores.append(score)

print(sorted(scores)[len(scores)//2])
    