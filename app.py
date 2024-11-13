from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import modules.weatherApi as weatherApi
import modules.attractions as attractions
import modules.restaurant as restaurant
import modules.hotels as hotels

app = Flask(__name__)

# Route to display the index page with the form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the location and dates from the form
        location = request.form['location']
        trip_start = request.form['trip_start']
        trip_end = request.form['trip_end']
        # Redirect to the itinerary page with the location and dates as URL parameters
        return redirect(url_for('itinerary', location=location, trip_start=trip_start, trip_end=trip_end))
    return render_template('index.html')

# Route to display the itinerary page
@app.route('/itinerary')
def itinerary():
    location = request.args.get('location')  # Retrieve the location from the URL

    with open('apikeys.json') as f:
        data = json.load(f)
        api = data['openweatherAPI_key']
        
    # Convert location to lat and lon
    loc_convert = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={api}"
    response = requests.get(loc_convert)
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    lat_lon = f"{lat},{lon}"

    # Get the dates and number of guests
    check_in = request.args.get('trip_start')
    check_out = request.args.get('trip_end')
    guests = 1

    # Call external modules to get data
    weather_list = weatherApi.get_weather(location)  # Fetch weather for the location
    attractions_list = attractions.main(lat_lon)  # Fetch attractions for the location
    restaurants_list = restaurant.get_restaurants(location)  # Fetch restaurants for the location
    hotel_list = hotels.Hotel_Api(lat, lon, check_in, check_out, guests)  # Fetch hotels for the location

    # Parse the information from the API responses
    try:
        weather_info = weather_list
    except:
        weather_info = "No weather found"
    
    try:
        attractions_info = attractions_list
    except:
        attractions_info = ['No attractions found']

    try:
        restaurants_info = []
        for i in range(len(restaurants_list[0])):
            number = restaurants_list[3][i] if restaurants_list[3][i] else "No number available"
            info = f"{restaurants_list[0][i]} | {restaurants_list[1][i]} | Rating: {restaurants_list[2][i]} | Number: {number}"
            restaurants_info.append(info)
    except:
        restaurants_info = ['No restaurants found']
    
    try:
        hotel_info = []
        for hotel in hotel_list:
            info = f"{hotel.get('title')} | {hotel.get('secondaryInfo')} | Rating: {hotel.get('bubbleRating')['rating']}"
            hotel_info.append(info)
    except:
        hotel_info = ['No hotels found']

    
    return render_template('itinerary.html', location=location, weather=weather_info, attractions=attractions_info, restaurants=restaurants_info, hotels=hotel_info)

if __name__ == '__main__':
    app.run(debug=True, port=80)