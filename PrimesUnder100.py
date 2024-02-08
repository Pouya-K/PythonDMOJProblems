import math
def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True
for i in range(2, 101):
    if isPrime(i) and i%10 == 7:
        print(i)