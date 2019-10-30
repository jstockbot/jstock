import random

hanguls = list("가나다라바마사아자차카타파하")

with open("d:/info2.txt", "w") as fileA:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        fileA.write("{},{},{}\n".format(name, weight, height))
