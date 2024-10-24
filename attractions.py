import requests
import json

with open('apikeys.json','r') as file:
    config = json.load(file)
    api_key = config['GoogleAPI']

def get_nearby_places( api_key,location, radius, place_type):
    
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    

    # Define the parameters for the API call
    params = {
        'location': location,
        'radius': radius,  # Radius in meters
        'type': place_type,  # Type of place (restaurant, park, etc.)
        'key': api_key
    }


    # Make the API request
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Parse the results
        results = response.json().get('results', [])
        return results
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    # Example coordinates: Latitude and Longitude (Central Park, NYC)
    location = '40.785091,-73.968285'
    radius = 1500  # 1500 meters
    place_type = 'park'  # Type of place to search for

    # Call the function to get nearby places
    places = get_nearby_places(api_key, location, radius, place_type)

    if places:
        # Print out the name of each place
        for place in places:
            name = place.get('name')
            address = place.get('vicinity')
            print(f"Place: {name}, Address: {address}")
    else:
        print("No places found.")

if __name__ == '__main__':
    main()




