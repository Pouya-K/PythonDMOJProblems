import sys

maxWeight = int(sys.stdin.readline())
numOfCars = int(sys.stdin.readline())
carWeights = []
for x in range(numOfCars):
    carWeights.append(int(sys.stdin.readline()))
carsPassed = 0
carsOnBridge = 0
currentWeight = 0
for i in range(numOfCars):
    currentWeight += carWeights[i]
    if currentWeight > maxWeight:
        break
    carsPassed += 1
    carsOnBridge += 1
    if carsOnBridge == 4:
        carsOnBridge = 3
        currentWeight -= carWeights[i - 3]
print(carsPassed)
