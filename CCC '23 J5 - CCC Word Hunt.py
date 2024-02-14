rows = int(input())
columns = int(input())
n = int(input())
grid = [[0 for c in range(columns)] for r in range(rows)]
totalGold = 0

for x in range(n):
    moves = input().split()
    num = int(moves[1]) - 1
    if moves[0] == "R":
        for x in range(columns):
            grid[num][x] += 1
    else:
        for x in range(rows):
            grid[x][num] += 1
for i in range(rows):
    for j in range(columns):
        if grid[i][j] % 2 == 1:
            totalGold += 1
print(totalGold)

# rows = int(input())
# columns = int(input())
# n = int(input())
# grid = [[False for c in range(columns)] for r in range(rows)]
# totalGold = 0
#
# for x in range(n):
#     moves = input().split()
#     num = int(moves[1]) - 1
#     if moves[0] == "R":
#         for x in range(columns):
#             grid[num][x] = not grid[num][x]
#     else:
#         for x in range(rows):
#             grid[x][num] = not grid[x][num]
# for i in range(rows):
#     for j in range(columns):
#         if grid[i][j]:
#             totalGold += 1
# print(totalGold)
