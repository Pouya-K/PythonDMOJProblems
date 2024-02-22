import sys

length = int(sys.stdin.readline())
arrayA = sys.stdin.readline().split()
arrayB = sys.stdin.readline().split()
defaultArrayA = []
defaultArrayB = []
for x in range(length):
    defaultArrayA.append(arrayA[x])
    defaultArrayB.append(arrayB[x])
moves = []
movesMade = 0
isPossible = True

for x in range(length):
    if arrayA[x] == arrayB[x]:
        continue
    if x != 0:
        if arrayA[x - 1] == arrayB[x]:
            movesMade += 1
            moves.append("R " + str(x - 1) + " " + str(x))
            arrayA[x] = arrayA[x - 1]
            continue
    if x == length - 1:
        isPossible = False
        break
    if arrayA[x + 1:length].count(arrayB[x]) > 0:
        firstFind = arrayA[x + 1:length].index(arrayB[x]) + x + 1
        if firstFind > x:
            movesMade += 1
            moves.append("L " + str(x) + " " + str(firstFind))
            for i in range(x, firstFind):
                arrayA[i] = arrayA[firstFind]
            continue
    isPossible = False
    if not isPossible:
        break

if isPossible:
    print("YES")
    print(movesMade)
    for line in moves:
        print(line)
else:
    isPossible = True
    moves = []
    movesMade = 0
    arrayA = defaultArrayA
    arrayB = defaultArrayB
    for x in range(length-1, -1, -1):
        if arrayA[x] == arrayB[x]:
            continue
        if x != length-1:
            if arrayA[x + 1] == arrayB[x]:
                movesMade += 1
                moves.append("L " + str(x) + " " + str(x+1))
                arrayA[x] = arrayA[x + 1]
                continue
        if x == 0:
            isPossible = False
            break
        if arrayA[0:x].count(arrayB[x]) > 0:
            firstFind = arrayA[0:x].index(arrayB[x])
            movesMade += 1
            moves.append("R " + str(firstFind) + " " + str(x))
            for i in range(firstFind+1, x+1):
                arrayA[i] = arrayA[firstFind]
            continue
        isPossible = False
        if not isPossible:
            break
    if isPossible:
        print("YES")
        print(movesMade)
        for line in moves:
            print(line)
    else:
        print("NO")