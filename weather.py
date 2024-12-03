import requests
import json
import pandas as pd
import time

# Configurable parameters
API_KEY = "4e837bcdfc489af8df9c72939b13b7f2"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
LOCATIONS = ["London", "New York", "Tokyo"]  # List of locations to fetch data for
UNITS = "metric"  # Options: 'metric' for Celsius, 'imperial' for Fahrenheit, 'standard' for Kelvin
OUTPUT_JSON_FILE = "weather_data.json"
OUTPUT_CSV_FILE = "weather_data.csv"

def fetch_weather_data(location, units, api_key):
    """Fetch weather data for a given location."""
    params = {
        'q': location,
        'units': units,
        'appid': api_key
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)  # Added timeout to avoid hanging
        response.raise_for_status()  # This will raise an error for bad HTTP status codes
        print(f"Requesting weather data for {location}...")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {location}: {e}")
        return None

def save_data_to_json(data, filename):
    """Save the fetched data to a JSON file."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {filename}")

def parse_json_to_csv(json_filename, csv_filename):
    """Parse the JSON file and save the relevant fields as a CSV."""
    with open(json_filename, 'r') as json_file:
        data = json.load(json_file)
    
    # Prepare a list to hold the rows for the CSV
    rows = []
    
    for location_data in data:
        if location_data:
            # Safely get the 'main' and 'wind' data
            weather_info = location_data.get('main', {})
            wind_info = location_data.get('wind', {})
            weather_desc = location_data.get('weather', [{}])[0].get('description', None)
            
            location_name = location_data.get('name', 'Unknown')
            weather_row = {
                'Location': location_name,
                'Temperature': weather_info.get('temp', None),
                'Feels Like': weather_info.get('feels_like', None),
                'Humidity': weather_info.get('humidity', None),
                'Pressure': weather_info.get('pressure', None),
                'Wind Speed': wind_info.get('speed', None),
                'Wind Direction': wind_info.get('deg', None),
                'Weather Description': weather_desc
            }
            rows.append(weather_row)

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(rows)
    df.to_csv(csv_filename, index=False)
    print(f"Data saved to {csv_filename}")

def main():
    # Fetch weather data for all locations
    all_weather_data = []
    for location in LOCATIONS:
        weather_data = fetch_weather_data(location, UNITS, API_KEY)
        if weather_data:
            all_weather_data.append(weather_data)
    
    # Save the initial response as JSON
    save_data_to_json(all_weather_data, OUTPUT_JSON_FILE)
    
    # Parse the saved JSON to CSV format
    parse_json_to_csv(OUTPUT_JSON_FILE, OUTPUT_CSV_FILE)

if __name__ == "__main__":
    main()