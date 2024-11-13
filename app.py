from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import weatherApi
import attractions
import restaurant
import hotels

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
        
    loc_convert = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={api}"
    response = requests.get(loc_convert)
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    lat_lon = f"{lat},{lon}"

    check_in = request.args.get('trip_start')
    check_out = request.args.get('trip_end')
    guests = 1

    # Call external modules to get data
    try:
        weather_info = weatherApi.get_weather(location)  # Fetch weather for the location
    except:
        weather_info = ['No weather found']
    attractions_list = attractions.get_nearby_places(lat_lon, 1500, 'park')  # Fetch attractions for the location
    restaurants_list = restaurant.get_restaurants(location)  # Fetch restaurants for the location
    hotel_list = hotels.Hotel_Api(lat, lon, check_in, check_out, guests)  # Fetch hotels for the location

    # Parse the information from the API response
    try:
        attractions_info = []
        for attraction in attractions_list:
            attractions_info.append(attraction.get('name') + ' | ' + attraction.get('vicinity') + '\n' + str(attraction.get('opening_hours').get('open_now'))
            + '\n' + str(attraction.get('rating', 'N/A')))
    except:
        attractions_info = ['No attractions found']

    try:
        restaurants_info = []
        for i in range(len(restaurants_list[0])):
            info = f"{restaurants_list[0][i]} | {restaurants_list[1][i]} | Rating: {restaurants_list[2][i]} | Number: {restaurants_list[3][i]}"
            restaurants_info.append(info)
    except:
        restaurants_info = ['No restaurants found']
    
    try:
        hotel_info = []
        for hotel in hotel_list:
            info = f"{hotel.get('title')} | {hotel.get('secondary_info')} | Rating: {hotel.get('bubble_rating')}"
            hotel_info.append(info)
    except:
        hotel_info = ['No hotels found']

    
    return render_template('itinerary.html', location=location, weather=weather_info, attractions=attractions_info, restaurants=restaurants_info)#, hotels=hotel_info)

if __name__ == '__main__':
    app.run(debug=True)



# TODO:
# * Make sure I am not missing anything and that all the code is updated to latest versions of modules
# * Clean up file structure and remove unnecessary files
# * CSS formatting for pages
# * Clean up code to look pretty