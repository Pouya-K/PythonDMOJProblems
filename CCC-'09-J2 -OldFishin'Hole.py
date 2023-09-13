troutPoint = int(input())
pikePoint = int(input())
pickerelPoint = int(input())
maxPoint = int(input())
counter = 0
for i in range(int(maxPoint / troutPoint + 1)):
    for j in range(int(maxPoint / pikePoint + 1)):
        for k in range(int(maxPoint / pickerelPoint + 1)):
            if troutPoint*i + pikePoint*j + pickerelPoint*k <= maxPoint and (i !=0 or j != 0 or k != 0):
                print(str(i) + " Brown Trout, " + str(j) + " Northern Pike, " + str(k) + " Yellow Pickerel")
                counter += 1
print("Number of ways to catch fish: " + str(counter))