data = input().split()
output = []


def isHeavyLight(datas):
    lastHeavy = datas.count(datas[0]) > 1
    for x in range(1, len(datas)):
        currentHeavy = datas.count(datas[x]) > 1
        if (currentHeavy and lastHeavy) or (not currentHeavy and not lastHeavy):
            return False
        lastHeavy = currentHeavy
    return True


for x in range(int(data[0])):
    line = input()
    if isHeavyLight(line):
        output.append("T")
    else:
        output.append("F")
for thing in output:
    print(thing)
