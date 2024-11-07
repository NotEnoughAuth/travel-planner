import requests
import json



# Get the API key from environment variables
with open('apikeys.json','r') as file:
        config = json.load(file)
        api_key = config['TRIPADVISOR_API_KEY']
        
def Hotel_Api(lat, long, check_in_date, check_out_date, guests):
    # API base URL for Amadeus Hotel Search
    base_url = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotelsByLocation"

    # Parameters to pass in the API request
    params = {
        "latitude": lat,
        "longitude": long,
        "checkIn": check_in_date,
        "checkOut": check_out_date,
        "adults": guests,
    }

    headers = {
        "x-rapidapi-key": api_key,
    }

    try:
        # Send the request to the API
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse and return the hotel data
        hotel_data = response.json()
        return hotel_data["data"]["data"]  # Assuming the API response contains a 'data' key with the results
    except requests.exceptions.RequestException as e:
        # Handle errors or failures
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Example usage:
    hotels = Hotel_Api("33.954737", "-118.212016", "2024-11-01", "2024-11-05", 2)
    if hotels:
        for hotel in hotels:
            print(f"Hotel: {hotel['title']}, Price: {hotel['priceForDisplay']}")
