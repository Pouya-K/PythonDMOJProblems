def converter(number: str, goingFrom: int, goingTo: int):
    base10Num = 0
    i = 0

    for letter in number[::-1]:
        if (letter.isdigit()):
            base10Num += int(letter) * goingFrom ** i
        else:
            base10Num += (ord(letter) - 55) * goingFrom ** i
        i += 1

    finalNum = ""

    while base10Num > 0:
        finalNum = str(base10Num % goingTo) + finalNum
        base10Num = int(base10Num / goingTo)

    print(number + " in base " + str(goingFrom) + " is " + finalNum + " in base " + str(goingTo) + ".")


converter("12AB", 16, 8)
