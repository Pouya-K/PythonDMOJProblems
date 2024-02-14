import sys

n = int(sys.stdin.readline())
heights = [int(x) for x in sys.stdin.readline().split()]
output = [0]


def findSymmetry(l, r):
    sum = 0
    while l <= r:
        sum += abs(heights[l] - heights[r])
        l += 1
        r -= 1
    return sum


for x in range(2, n + 1):
    lowestSymmetry = float("inf")
    for i in range(n - x + 1):
        lowestSymmetry = min(lowestSymmetry, findSymmetry(i, i + x - 1))
    output.append(lowestSymmetry)

print(*output)
