import math

list = []


def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True


def findPrimeAdd(n):
    n1, n2, doubleN = n, n, 2 * n
    found = False
    while not found:
        if isPrime(n1) and isPrime(n2):
            found = True
        else:
            n1 -= 1
            n2 += 1
    list.append((n1, n2))


for i in range(int(input())):
    findPrimeAdd(int(input()))

for x in list:
    print(f'{x[0]} {x[1]}')

