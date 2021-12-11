lis = []
with open("10.txt", "r") as f:
    for line in f:
        lis.append(line.rstrip())
chars = {"(":")", "[":"]", "{":"}", "<":">"}
points = {")":3, "]":57, "}":1197, ">":25137}
values = []
score = 0
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
            values.append(char)
            break
for value in values:
    score += points[value]
print(score)