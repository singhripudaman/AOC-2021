lis = []
with open("9.txt", "r") as f:
    for line in f:
        lis.append(line.rstrip())
low = []
def edgeCheck(i, j, num, lis):
    if i == 0 and j == 0:                                   #top left
        if num < lis[i+1][j] and num < lis[i][j+1]:
            return True
    elif i == 0 and j == (len(lis[0])-1):                   #top right
        if num < lis[i+1][j] and num < lis[i][j-1]:
            return True
    elif i == (len(lis)-1) and j == 0:                      #bottom left
        if num < lis[i-1][j] and num < lis[i][j+1]:
            return True
    elif i == (len(lis)-1) and j == (len(lis[0])-1):        #bottom right
        if num < lis[i][j-1] and num < lis[i-1][j]:
            return True
    else:
        if i == 0:
            if num < lis[i][j-1] and num < lis[i][j+1] and num < lis[i+1][j]:
                return True
        if j == 0:
            if num < lis[i-1][j] and num < lis[i+1][j] and num < lis[i][j+1]:
                return True
        if i == (len(lis)-1):
            if num < lis[i][j-1] and num < lis[i][j+1] and num < lis[i-1][j]:
                return True
        if j == (len(lis[0])-1):
            if num < lis[i-1][j] and num < lis[i+1][j] and num < lis[i][j-1]:
                return True

def check(i, j, num, lis):
    if (i != 0) and (j!= 0) and (i != (len(lis)-1)) and (j != len(lis[0])-1):
        if (num < lis[i-1][j]) and (num < lis[i+1][j]) and (num < lis[i][j-1]) and (num < lis[i][j+1]):
            return True
        return False
    elif edgeCheck(i, j, num, lis):
        return True
    else:
        return False  

for i in range(len(lis)):
    for j in range(len(lis[0])):
        if check(i, j, lis[i][j], lis):
            low.append(lis[i][j])

low = [int(entry) for entry in low]
print(sum(low) + len(low))