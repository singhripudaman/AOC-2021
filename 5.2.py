import re
lis = []
with open("5.txt", "r") as f:
    pattern = re.compile(r"([0-9]{1,3}),([0-9]{1,3}) -> ([0-9]{0,3}),([0-9]{1,3})")
    for line in f:
        match = pattern.match(line)
        lis.append((int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))
visited = {}
for points in lis:
    x1, y1, x2, y2, = points
    if (x1 == x2) and (y1 < y2):        
        for num in range(y1, y2 + 1):
            if (x1, num) in visited:
                visited[(x1, num)] += 1
            else:
                visited[(x1, num)] = 1
    elif (x1 == x2) and (y1 >= y2):       
        for num in range(y2, y1 + 1):
            if (x1, num) in visited:
                visited[(x1, num)] += 1
            else:
                visited[(x1, num)] = 1
    elif (y1 == y2) and (x1 < x2):        
        for num in range(x1, x2 + 1):
            if (num, y1) in visited:
                visited[(num, y1)] += 1
            else:
                visited[(num, y1)] = 1
    elif (y1 == y2) and (x1 >= x2):       
        for num in range(x2, x1 + 1):
            if (num, y1) in visited:
                visited[(num, y1)] += 1
            else:
                visited[(num, y1)] = 1

    if (x1 != x2) and (y1 != y2):
        x = x1
        y = y1
        while x != x2 and y != y2:
            if (x, y) in visited:
                visited[(x,y)] += 1
            else:
                visited[(x,y)] = 1
            x += 1 if x1 < x2 else -1
            y += 1 if y1 < y2 else -1
            if x == x2 and y == y2:
                if (x, y) in visited:
                    visited[(x,y)] += 1
                else:
                    visited[(x,y)] = 1

answer = 0      
for keys in visited:
    if visited[keys] >= 2:
        answer += 1
print(answer)

