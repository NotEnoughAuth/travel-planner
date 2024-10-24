import requests # type: ignore
import json

with open('apikeys.json') as f:
        api_data = json.load(f)
        api_key = api_data['{dbc186abbdmsh821a1681fa1333ap152100jsnf9c1d76adf45}_api_key']


def Hotel_Api(location, check_in_date, check_out_date, guests):
    # API base URL for Amadeus Hotel Search
    base_url = "tripadvisor16.p.rapidapi.com"
    
    
 
    
    # Parameters to pass in the API request
    params = {
        "cityCode": location,  # Use IATA city code
        "checkInDate": check_in_date,
        "checkOutDate": check_out_date,
        "adults": guests,
        "apikey": api_key
    }
    
    try:
        # Send the request to the API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse and return the hotel data
        hotel_data = response.json()
        return hotel_data.get('data', [])  # Assuming the API response contains a 'data' key with the results
    except requests.exceptions.RequestException as e:
        # Handle errors or failures
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Example usage:
    hotels = Hotel_Api("NYC", "2024-11-01", "2024-11-05", 2)
    if hotels:
        for hotel in hotels:
            print(f"Hotel: {hotel['name']}, Price: {hotel['price']}")