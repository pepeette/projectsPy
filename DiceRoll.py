import random

reply = "Y"

while reply == "Y":
    dice = random.randint(1, 6)
    if dice == 1:
        print("--------")
        print("|      |")
        print("|   1  |")
        print("|      |")
        print("--------")
        print("        ")

    elif dice == 2:
        print("--------")
        print("|      |")
        print("|   2  |")
        print("|      |")
        print("--------")
        print("        ")

    elif dice == 3:
        print("--------")
        print("|      |")
        print("|   3  |")
        print("|      |")
        print("--------")
        print("        ")

    elif dice == 4:
        print("--------")
        print("|      |")
        print("|   4  |")
        print("|      |")
        print("--------")
        print("        ")

    elif dice == 5:
        print("--------")
        print("|      |")
        print("|   5  |")
        print("|      |")
        print("--------")
        print("        ")

    elif dice == 6:
        print("--------")
        print("|      |")
        print("|   6  |")
        print("|      |")
        print("--------")
        print("        ")
    reply = input("Press Y to roll again")


