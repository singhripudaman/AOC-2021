with open("11.txt", "r") as f:
    data = [line.rstrip() for line in f]
lis = [[int(num) for num in entry] for entry in data]
def solve(i, j, lis, visited):
    if i < 0 or j < 0 or i >= len(lis) or j >= len(lis[0]):
        return 0
    if lis[i][j] == 0:
        return 0
    if (i,j) in visited:
        visited.remove((i,j))
    else: lis[i][j] += 1
    if lis[i][j] >= 10:
        lis[i][j] = 0
        return 1 + solve(i+1, j, lis, visited) + solve(i, j+1, lis, visited) +\
            solve(i-1, j, lis, visited) + solve(i, j-1, lis, visited) + \
                solve(i+1, j+1, lis, visited) + solve(i+1, j-1, lis, visited) + \
                        solve(i-1, j-1, lis, visited) + solve(i-1, j+1, lis, visited)
    else: return 0

def main(steps):
    count = 0
    for step in range(steps):
        visited = []
        for i in range(len(lis)):
            for j in range(len(lis[0])):
                lis[i][j] += 1
                visited.append((i,j))
        for i in range(len(lis)):
            for j in range(len(lis[0])):
                count += solve(i, j, lis, visited)
    return count

print(main(100))
