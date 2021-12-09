with open("7.txt", "r") as f:
    lis = f.read().split(",")
lis = [int(num) for num in lis]

smallest = float("inf")
for i in range(min(lis), max(lis)+1):
    sums = 0
    for j in range(len(lis)):
        num = abs(i-lis[j])
        sums += (num * (num + 1)) // 2
    if sums < smallest:
        smallest = sums
print(smallest)

