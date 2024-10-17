import requests

def Hotel_Api(location, check_in_date, check_out_date, guests):

    # API base URL (example: you need the real API URL from the service you are using)
    base_url = "https://example-hotel-api.com/search"
    
    # Your API key (replace with your actual API key)
    api_key = "L7nJ1GJDTZjOZ55TAwMIbUc9gMUsgGBe"
    
    # Parameters to pass in the API request
    params = {
        "location": location,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date,
        "guests": guests,
        "apikey": api_key
    }
    
    # Send the request to the API
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        # Parse and return the hotel data
        hotel_data = response.json()
        return hotel_data['hotels']  # Assuming the API response contains a 'hotels' key with the results
    else:
        # Handle errors or failures
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Example usage:
hotels = Hotel_Api("New York", "2024-11-01", "2024-11-05", 2)
if hotels:
    for hotel in hotels:
        print(f"Hotel: {hotel['name']}, Price: {hotel['price']}")

