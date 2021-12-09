from math import prod
lis = []
with open("9.txt", "r") as f:
    for line in f:
        temp = line.rstrip()
        lis.append([char for char in temp])
lis = [[int(num) for num in entry] for entry in lis]

def floodFill(i, j, lis):
    if i < 0 or j < 0 or i >= len(lis) or j >= len(lis[0]):
        return 0
    if lis[i][j] == 9:
        return 0
    lis[i][j] = 9
    return 1 + floodFill(i+1, j, lis) + floodFill(i, j+1, lis) + floodFill(i-1, j, lis) + floodFill(i, j-1, lis)
        
def main():
    basins = []
    for i in range(len(lis)):
        for j in range(len(lis[0])):
            basins.append(floodFill(i, j, lis))
    basins = sorted(basins)[-3:]
    return prod(basins)

print(main())
