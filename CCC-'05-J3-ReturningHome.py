startingDirection = input()
list = []
if startingDirection == "R":
    list.append("Turn LEFT into your HOME.")
else:
    list.append("Turn RIGHT into your HOME.")
while True:
    street = input()
    if street == "SCHOOL":
        break
    if input() == "R":
        list.append("Turn LEFT onto " + street + " street.")
    else:
        list.append("Turn RIGHT onto " + street + " street.")
for i in range(len(list)-1, -1, -1):
    print(list[i])