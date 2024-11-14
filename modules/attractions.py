import requests
import json
import datetime

with open('/app/apikeys.json','r') as file:
        try:
            config = json.load(file)
            api_key = config['GoogleAPI']
        except:
            print("could not load " + file)
            exit()

def get_day_of_week():
    current_day = datetime.datetime.now().weekday()
    return current_day

def get_nearby_places(location, radius, place_type):
    
    

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
    

# Function to get place details using place_id
def get_place_details(place_id):
    details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
    response = requests.get(details_url)
    return response.json().get("result", {})



def main(location):
    # Example coordinates: Latitude and Longitude (Central Park, NYC)
    #location = '44.8113,-91.4985'
    radius = 1500  # 1500 meters
    place_type = 'tourist_attraction'  # Type of place to search for

    # Call the function to get nearby places
    places = get_nearby_places(location, radius, place_type)
    day = get_day_of_week()

    attractions = []
    
    if places:
        for place in places:
            name = place.get('name')
            place_id = place.get('place_id') 
        
            place_details = get_place_details(place_id)
        
            opening_hours = place_details.get('opening_hours', {}).get('weekday_text', [])

            formatted_address = place_details.get('formatted_address', '')
            address_components = place_details.get('address_components', [])
        
            if formatted_address:
                address_lines = formatted_address.split(',')
                street_address = address_lines[0].strip()  
                city = address_lines[1].strip() if len(address_lines) > 1 else ""
            
            if opening_hours:
                hours = opening_hours[day]
            else:
                hours = 'No Hours Listed'

            price_level = place_details.get('price_level')
            attractions.append(f"{name}\n{street_address} {city}\n{hours}")

        return attractions
    else:
        print("No places found.")

if __name__ == '__main__':
    main()




