infile = open("1.txt", "r")
lis = []
for line in infile:
    line = line.strip()
    lis.append(int(line))
infile.close()
a = lis[0] + lis[1] + lis[2]
larger = 0
for i in range(1, len(lis)-2):
    add = lis[i] + lis[i+1] + lis[i+2]
    if add > a:
        larger += 1
    a = add
print(larger)

