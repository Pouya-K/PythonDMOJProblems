a =  int(input())
if a <= 5:
    print(int(a/2) + 1)
else:
    counter = 0
    for i in range(1, int(a/2 + 1)):
        if a-i <= 5:
            counter += 1
    print(counter)