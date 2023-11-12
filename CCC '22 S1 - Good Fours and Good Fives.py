number = int(input())
numberOfWays = 0
for x in range(int(number/5) + 1):
    if (number - 5*x)%4 == 0: numberOfWays += 1
print(numberOfWays)