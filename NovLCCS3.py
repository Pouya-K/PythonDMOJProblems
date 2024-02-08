import math

a, b = input().split()
a = int(a)
b = int(b)

if math.log(a, b) > a/b:
    print("Bacteria on yeast.")
else:
    print("Yeast on bacteria.")
