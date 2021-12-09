lis = []
with open("3.txt", "r") as f:
    for line in f:
        lis.append(line.rstrip())
gamma = ""
epsilon = ""
for i in range(len(lis[0])):
    counter = 0
    for j in range(len(lis)):
        if lis[j][i] == "1":
            counter += 1
    if counter > (len(lis) - counter):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
print(int(gamma, 2) * int(epsilon, 2))

