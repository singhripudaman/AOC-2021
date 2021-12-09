import re
from itertools import permutations
pattern = re.compile(r'([A-Z a-z]+) \| ([A-Z a-z]+)')
lis = []
with open("8.txt", "r") as f:
    for line in f:
        match = pattern.match(line)
        lis.append(((match.group(1)), match.group(2)))

answer = 0
for tup in lis:
    left, right = tup
    temp = left.split()
    zero = ""
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    seven = ""
    eight = ""
    nine = ""

    for word in temp:
        if (len(word) == 4):
            four = word
        if (len(word) == 7):
            eight = word
        if (len(word) == 2):
            one = word
        if (len(word) == 3):
            seven = word
    for word in temp:
        if (len(word) == 6):
            count = 0
            for char in four:
                if char in word:
                    count += 1
            if count == 4:
                nine = word
                continue
            count = 0
            for char in seven:
                if char in word:
                    count += 1
            if count == 3:
                zero = word
                continue
            six = word
        if (len(word) == 5):
            count = 0
            for char in seven:
                if char in word:
                    count += 1
            if count == 3:
                three = word
                continue
            count = 0
            for char in four:
                if char in word:
                    count += 1
            if count == 3:
                five = word
                continue
            two = word
    temp = right.split()
    data = ""
    for word in temp:
        a = list(permutations(zero))
        a = ["".join(element) for element in a]
        if word in a:
            data += "0"
        a = list(permutations(one))
        a = ["".join(element) for element in a]
        if word in a:
            data += "1"
        a = list(permutations(two))
        a = ["".join(element) for element in a]
        if word in a:
            data += "2"
        a = list(permutations(three))
        a = ["".join(element) for element in a]
        if word in a:
            data += "3"
        a = list(permutations(four))
        a = ["".join(element) for element in a]
        if word in a:
            data += "4"
        a = list(permutations(five))
        a = ["".join(element) for element in a]
        if word in a:
            data += "5"
        a = list(permutations(six))
        a = ["".join(element) for element in a]
        if word in a:
            data += "6"
        a = list(permutations(seven))
        a = ["".join(element) for element in a]
        if word in a:
            data += "7"
        a = list(permutations(eight))
        a = ["".join(element) for element in a]
        if word in a:
            data += "8"
        a = list(permutations(nine))
        a = ["".join(element) for element in a]
        if word in a:
            data += "9"
    answer += int(data)

print(answer)