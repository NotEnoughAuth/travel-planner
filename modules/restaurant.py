import requests
import json

'''This function get the information of nearby restaurants.'''
def get_restaurants(city):
    business_names = []
    locations = []
    numbers = []
    ratings = []
    
    # Load the Yelp API key
    with open('/app/apikeys.json') as f:
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
        rating = business['rating']
        ratings.append(rating)
        
        #Phone number
        number = business['display_phone']
        numbers.append(number)

    return business_names, locations, ratings, numbers


if __name__ == "__main__":
    #This is how this function should be implemented in the main function
    restaurants, r_location, r_price, r_phone =  get_restaurants("New York City")
    print("Here are some local restaurants you may be interested in:")
    for a, b, c, d in zip(restaurants, r_location, r_price, r_phone):
        print(f"{a}, {b}, {c}, {d}")
