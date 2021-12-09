import re
pattern = re.compile(r'([A-Z a-z]+) \| ([A-Z a-z]+)')
lis = []
with open("8.txt", "r") as f:
    for line in f:
        match = pattern.match(line)
        lis.append(((match.group(1)), match.group(2)))

def countCommon(first, second):
    count = 0
    for char in first:
        if char in second:
            count += 1
    return count

answer = 0
for tup in lis:
    left, right = tup
    temp = left.split()
    dic = {}
    for i in range(10):
        dic[i] = ""

    for word in temp:
        length = len(word)
        if length == 4:
            dic[4] = word
        if length == 7:
            dic[8] = word
        if length == 2:
            dic[1] = word
        if length == 3:
            dic[7] = word

    for word in temp:
        length = len(word)
        if length == 6:
            if countCommon(dic[4], word) == 4:
                dic[9] = word
            elif countCommon(dic[7], word) == 3:
                dic[0] = word
            else:
                dic[6] = word
        elif length == 5:
            if countCommon(dic[7], word) == 3:
                dic[3] = word
            elif countCommon(dic[4], word) == 3:
                dic[5] = word
            else:
                dic[2] = word


    temp = right.split()
    data = ""

    for word in temp:
        for key, value in dic.items():
            if sorted(word) == sorted(value):
                data += str(key)
    answer += int(data)

print(answer)