with open("6.txt", "r") as f:
    lis = f.read().split(",")
lis = [int(num) for num in lis]

for days in range(80):
    toBeAdded = 0
    for num, age in enumerate(lis):
        lis[num] -= 1
        if lis[num] == -1:
            toBeAdded += 1
            lis[num] = 6
    for i in range(toBeAdded):
        lis.append(8)
print(len(lis))

