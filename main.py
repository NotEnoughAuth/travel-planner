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
    
    formattedLat = "{:.6f}".format(float(randomPlace[3]))
    formattedLong = "{:.6f}".format(float(randomPlace[4]))

    outputjson = {
        "city": randomPlace[0],
        "latlong": formattedLat + "," + formattedLong,
        "state": randomPlace[1],
    }

    return outputjson


if __name__ == "__main__":
    print("=============================================================================")
    print("Hello fellow Traveler!")
    legallyDistinctInput = input("Please type out a location that you want to travel to:\n\nLocation: ")


    print("\n\n\n\n")
    yn = yesnoinput("Are you really sure you want to travel to: " + legallyDistinctInput)

    if yn == True:
        if yesnoinput("Are you sure, I herd its warmer in Austin Texas: "):
            print("Fine we will go to " + legallyDistinctInput)
            loc = input("Please enter the latitude and longitude of " + legallyDistinctInput)
            city = legallyDistinctInput
        else:
            city = "Austin"
            print("Glad you came to your senses, we will be going to " + city)
            loc = input("Please enter the latitude and longitude of " + city)
    else:
        print("\nPicking random place to go to...")
        randomCity = randomPlace()
        city = randomCity["city"]
        loc = randomCity["latlong"]
        print("We will be going to " + city + ", " + randomCity["state"])
    
    print("\n\n")

    print("=============================================================================")
    print("\n")
    print("Getting the weather for " + city)
    print("\t" + get_weather(city))
    print("\n")
    print("=============================================================================")
    print("\n")
    print("Getting nearby parks in " + city)
    parks = get_nearby_places(loc, 1500, 'park')
    if parks:
        for park in parks:
            print("\t" + park['name'])
    else:
        print("\t" + "No parks found")
    print("\n")
    print("=============================================================================")
    print("\n")
    print("Getting nearby restaurants in " + city)
    resturants = get_restaurants(city)

    for restaurant in resturants[0]:
        print("\t" + restaurant)
    print("\n")
    print("=============================================================================")
    print("\n")
    print("Hotel Planning Page")
    cityCode = input("Please enter the IANA city code of the location you want to travel to: ")
    checkInDate = input("Please enter the check-in date (YYYY-MM-DD): ")
    checkOutDate = input("Please enter the check-out date (YYYY-MM-DD): ")
    adults = input("Please enter the number of adults: ")
    hotels = Hotel_Api(cityCode, checkInDate, checkOutDate, adults)
    if hotels:
        for hotel in hotels:
            print(f"Hotel: {hotel['name']}, Price: {hotel['price']}")