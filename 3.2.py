lis = []
with open("3.txt", "r") as f:
    for line in f:
        lis.append(line.rstrip())
gamma = ""
epsilon = ""
copy = list(lis)
for i in range(len(lis[0])):
    counter = 0
    for j in range(len(lis)):
        if lis[j][i] == "1":
            counter += 1
    if counter >= (len(lis) - counter):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
    lis = [field for field in lis if field[i] == gamma[-1]]
    if len(lis) == 1:
        break

for i in range(len(copy[0])):
    counter = 0
    for j in range(len(copy)):
        if copy[j][i] == "1":
            counter += 1
    if counter >= (len(copy) - counter):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
    copy = [field for field in copy if field[i] == epsilon[-1]]
    if len(copy) == 1:
        break
print(int(lis[0], 2) * int(copy[0], 2))

