file = open("day1-data.txt")
digits = "0123456789"
alphabet = "abcdefghijklmnopqrstuvwxyz\n"
numbers = {"zero": 0, "one": 1, "two": 2, "three": 3, "four":4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine":9}
calibrationValues = []
lineNumber = 0

for line in file:
    lineNumber = lineNumber + 1
    charNumber = 0
    digits = []
    for x in line:
        charNumber = charNumber + 1
        if str(x) not in alphabet:
            digits.append(x)
        else:
            for number in numbers:
                segment = line[charNumber-1 : charNumber+6]
                if segment.startswith(number):
                    digits.append(numbers[number])
                    break

    calibrationValues.append(str(digits[0])+str(digits[len(digits)-1]))

    # if lineNumber > 1:
    #     break

total = 0
for y in calibrationValues:
    total = total + int(y)


print(total)
# 55614 is correct answer!
file.close()
