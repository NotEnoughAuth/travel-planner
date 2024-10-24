import csv
import random
from weatherApi import get_weather


def yesnoinput(prompt):
    legallyDistinctInput = input(prompt + " [Y\\n] ")
    if legallyDistinctInput is None or legallyDistinctInput == "":
        return True
    elif legallyDistinctInput.lower() == "yes" or legallyDistinctInput.lower() == "y":
        return True
    elif legallyDistinctInput.lower() == "no" or legallyDistinctInput.lower() == "n":
        return False


def randomPlace():
    # read places.csv and find a random value
    # print that value

    with open('places.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        places = list(csv_reader)

    # get random number from 0 to len(places)
    random_number = random.randint(0, len(places))

    randomPlace = places[random_number]


    return randomPlace[0] + ", " + randomPlace[1]


print("=============================================================================")
print("Hello fellow Traveler!")
legallyDistinctInput = input("Please type out a location that you want to travel to:\n\nLocation: ")


print("\n\n\n\n")
yn = yesnoinput("Are you really sure you want to travel to: " + legallyDistinctInput)

if yn == True:
    if yesnoinput("Are you sure, I herd its warmer in Austin Texas: "):
        print("Fine we will go to " + legallyDistinctInput)
    else:
        new_loc = "Austin, Texas"
        print("Glad you came to your senses, we will be going to " + new_loc)
else:
    print("\nPicking random place to go to...")
    print(randomPlace())
    new_loc = randomPlace()

print("\n\n\n\n")


print("=============================================================================")

get_weather(new_loc)