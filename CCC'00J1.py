num1, num2 = [int(i) for i in input().split()]
print("Sun Mon Tue Wed Thr Fri Sat")
print(" "*(4*(num1-1)), end="")
for i in range(1, num2+1):
    if i < 10:
        print(" ", end="")
    if (i + num1 - 1) % 7 == 0 and i != num2:
        print(" " + str(i))
    elif i == num2:
        print(" " + str(i), end="")
    else:
        print(" " + str(i) + " ", end="")