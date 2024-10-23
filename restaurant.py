import requests
import os
import json
from pprint import pprint

'''This function get the information of nearby restaurants.'''
def get_restaurants(city):
    business_names = []
    locations = []
    numbers = []
    price_ranges = []
    # Load the Yelp API key
    with open('apikeys.json') as f:
        api_data = json.load(f)
        api_key = api_data['yelp_api_key']

    # Send a GET request to the Yelp API
    url = f"https://api.yelp.com/v3/businesses/search?location={city}&term=restaurants&categories=&sort_by=best_match&limit=5"
    headers = {
        "accept": "application/json",
        "Authorization": api_key
    }
    
    #Process request
    response = requests.get(url, headers=headers)
    data = response.json()
    #Work with parsed data to create lists
    for business in data['businesses']:
        #Business names
        name = business['name']
        business_names.append(name)
        #Locations
        location_json = business['location']['display_address']
        location = ', '.join(location_json)
        locations.append(location)
        #Rating
        price = business['rating']
        price_ranges.append(price)
        #Phone number
        number = business['display_phone']
        numbers.append(number)

    print("Here are some restaurants in your area that you might be interested in:")
    for a, b, c, d in zip(business_names, locations, price_ranges, numbers):
        print(f"{a}, {b}, {c}, {d}")

if __name__ == "__main__":
    get_restaurants("Menomonie, WI")
    