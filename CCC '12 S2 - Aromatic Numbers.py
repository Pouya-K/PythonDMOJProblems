totalSum = 0
data = input()
symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
numBefore = [int(data[0]), data[1]]
for x in range(2, len(data) - 1, 2):
    arabicNum = int(data[x])
    romanNum = data[x + 1]
    if symbols[romanNum] > symbols[numBefore[1]]:
        numBefore[0] = -1 * numBefore[0]
    totalSum += numBefore[0] * symbols[numBefore[1]]
    numBefore = [arabicNum, romanNum]
totalSum += numBefore[0] * symbols[numBefore[1]]
print(totalSum)
