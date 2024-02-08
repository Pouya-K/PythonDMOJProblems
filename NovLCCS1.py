n, r, c = input().split()
n = int(n)
r = int(r)
c = int(c)
line = [input().split(), input().split()]
countedPlaces = []
def findSpaces(row, col):
    global line, countedPlaces
    if line[row - 1][col - 1] == "0" and not((r, c) in countedPlaces):
        countedPlaces.append((r, c))
        if col!=1:
            findSpaces(row, col-1)
            if row == 2:
                findSpaces(row - 1, col-1)
            else:
                findSpaces(row + 1, col - 1)
        if col!=5:
            findSpaces(row, col+1)
            if row == 2:
                findSpaces(row - 1, col+1)
            else:
                findSpaces(row + 1, col + 1)
        if row == 2:
            findSpaces(row - 1, col)
        else:
            findSpaces(row + 1, col)
findSpaces(r, c)
print(len(countedPlaces))