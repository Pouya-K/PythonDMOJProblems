n = int(input())

firstNum = int(input())
firstHalf = []
secondHalf = []
answer = 0

for x in range (int(n/2) - 1):
    firstHalf.append(int(input()))

if int(input()) == firstNum:
    answer += 2
for x in range (int(n/2) - 1):
    if int(input()) == firstHalf[x]:
        answer += 2

print(answer)