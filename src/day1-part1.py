file = open("day1-data.txt")
digits = "0123456789"
alphabet = "abcdefghijklmnopqrstuvwxyz\n"
calibrationValues = []
lineNumber = 0

for line in file:
    lineNumber = lineNumber + 1
    print(lineNumber, line)

    charNumber = 0
    digits = []
    for x in line:
        charNumber = charNumber + 1
        if str(x) not in alphabet:
            print(x)
            digits.append(x)
            print(digits)

    calibrationValues.append(str(digits[0])+str(digits[len(digits)-1]))
    print(calibrationValues)

    if lineNumber > 2:
        break


total = 0
for y in calibrationValues:
    total = total + int(y)


print(total)
# 55488 correct answer!
file.close()
