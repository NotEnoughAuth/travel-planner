import csv
import random
from weatherApi import get_weather
from attractions import get_nearby_places
from restaurant import get_restaurants
from module1 import Hotel_Api


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
        city = "Austin, Texas"
        print("Glad you came to your senses, we will be going to " + city)
else:
    print("\nPicking random place to go to...")
    print(randomPlace())
    city = randomPlace()

print("\n\n\n\n")

loc = input("Please enter the latitude and longitude of the location you want to travel to: ")

print("=============================================================================")

print("Getting the weather for " + city)
print(get_weather(city))

print("=============================================================================")
print("Getting nearby parks in " + city)
print(get_nearby_places(loc, 1500, 'park'))

print("=============================================================================")
print("Getting nearby restaurants in " + city)
print(get_restaurants(city))

print("=============================================================================")
print("Hotel Planning Page")
cityCode = input("Please enter the IANA city code of the location you want to travel to: ")
checkInDate = input("Please enter the check-in date (YYYY-MM-DD): ")
checkOutDate = input("Please enter the check-out date (YYYY-MM-DD): ")
adults = input("Please enter the number of adults: ")

print(Hotel_Api(cityCode, checkInDate, checkOutDate, adults))
