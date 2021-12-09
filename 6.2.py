with open("6.txt", "r") as f:
    lis = f.read().split(",")
lis = [int(num) for num in lis]

nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for num in lis: 
    nums[num] += 1
for days in range(256):
    value = nums[0]
    for i in range(len(nums) - 1):
        nums[i] = nums[i+1]
    nums[8] = value
    nums[6] += value
print(sum(nums))

