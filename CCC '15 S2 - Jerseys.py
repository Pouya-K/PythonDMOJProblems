import sys

numOfJersey = int(sys.stdin.readline())
numOfAthletes = int(sys.stdin.readline())
requestsMade = 0

jerseys = []
jerseysTaken = []
sizes = {
    "S": 0,
    "M": 1,
    "L": 2
}
for x in range(numOfJersey):
    jerseys.append(sizes[sys.stdin.readline().strip()])
    jerseysTaken.append(False)
for i in range(numOfAthletes):
    data = sys.stdin.readline().split()
    preferredSize = sizes[data[0]]
    jerseyNum = int(data[1]) - 1
    if jerseys[jerseyNum] >= preferredSize and not jerseysTaken[jerseyNum]:
        requestsMade += 1
        jerseysTaken[jerseyNum] = True

print(requestsMade)