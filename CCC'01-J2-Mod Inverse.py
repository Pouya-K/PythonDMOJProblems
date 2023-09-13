x = int(input())
m = int(input())
for i in range(m):
    if (i * x) % m == 1:
        print(i)
        break
    elif i == m-1:
        print("No such integer exists.")