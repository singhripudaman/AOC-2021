infile = open("1.txt", "r")
lis = []
for line in infile:
    line = line.strip()
    lis.append(int(line))
infile.close()
larger = 0
for i in range(1, len(lis)):
    if lis[i] > lis[i-1]:
        larger += 1
print(larger)

