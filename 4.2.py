numbers = []
lis = []
data = []
parsed = []
with open("4.txt", "r") as f:
    line = f.readline().rstrip()
    numbers.append(line)
    lis = f.read().split("\n\n")
numbers = numbers[0].split(",")


for field in lis:
    data.append(field.split("\n"))
for entry in data:
    for field in entry:
        parsed.append(field.split())
parsed = parsed[1:]
lis = []
for i in range(0, len(parsed), 5):
    another = []
    for j in range(i, i + 5):
        another.append(parsed[j])
    lis.append(another)

def checkRows(board):
    for row in board:
        count = 0
        for num in row:
            if num == "*":
                count += 1
        if count == 5:
            return True
    return False

def checkColumns(board):
    for i in range(len(board[0])):
        count = 0
        for j in range(len(board)):
            if board[j][i] == "*":
                count += 1
        if count == 5:
            return True
    return False
def main():
    for number in numbers:
        for i in range(len(lis)):                   #list
            for j in range(len(lis[0])):            #board
                for k in range(len(lis[0][0])):     #row
                    if lis[i][j][k] == number:
                        lis[i][j][k] = "*"
        for board in lis:
            if (checkColumns(board) or checkRows(board)) and (len(lis) !=1):
                lis.remove(board)
            else:
                if (checkColumns(board) or checkRows(board)):
                    for board in lis:
                        answer = 0
                        for row in board:
                            for num in row:
                                if num.isnumeric():
                                    answer += int(num)
                        answer *= int(number)
                        return answer
                
print(main())
