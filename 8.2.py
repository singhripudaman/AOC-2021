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
    zero = one = two = three = four = five = six = seven = eight = nine = ""

    for word in temp:
        length = len(word)
        if length == 4:
            four = word
        if length == 7:
            eight = word
        if length == 2:
            one = word
        if length == 3:
            seven = word

    for word in temp:
        length = len(word)
        if length == 6:
            if countCommon(four, word) == 4:
                nine = word
            elif countCommon(seven, word) == 3:
                zero = word
            else:
                six = word
        elif length == 5:
            if countCommon(seven, word) == 3:
                three = word
            elif countCommon(four, word) == 3:
                five = word
            else:
                two = word

    temp = right.split()
    data = ""

    for word in temp:
        word = sorted(word)
        if word == sorted(zero):
            data += "0"
        elif word == sorted(one):
            data += "1"
        elif word == sorted(two):
            data += "2"
        elif word == sorted(three):
            data += "3"
        elif word == sorted(four):
            data += "4"
        elif word == sorted(five):
            data += "5"
        elif word == sorted(six):
            data += "6"
        elif word == sorted(seven):
            data += "7"
        elif word == sorted(eight):
            data += "8"
        elif word == sorted(nine):
            data += "9"
    answer += int(data)

print(answer)