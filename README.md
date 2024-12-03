# Weather Data Extractor

## Description
This Python script fetches weather data from OpenWeatherMap API for specified locations, saves the data in JSON format, and processes it into a CSV file (excluding the weather array). 

## Setup Instructions
1. **Sign up for OpenWeatherMap**: 
   - Go to [OpenWeatherMap](https://openweathermap.org/), create an account, and get an API key.
   
2. **Configure the script**:
   - Open the `weather_extractor.py` script.
   - Replace the placeholder `YOUR_API_KEY` in the `config` dictionary with your actual OpenWeatherMap API key.
   
3. **Install dependencies**:
   - Install the required Python libraries by running:
     ```bash
     pip install requests
     ```

4. **Run the script**:
   - Execute the script by running:
     ```bash
     python weather_extractor.py
     ```

5. **Generated Files**:
   - The script will fetch weather data for the locations specified in the `config` dictionary, save it to `weather_data.json`, and convert the data into `weather_data.csv`.

## Example Outputs:
- **weather_data.json**: Contains raw JSON weather data from OpenWeatherMap API.
- **weather_data.csv**: A CSV file with weather details (excluding the weather array), with fields like `city`, `temperature`, `humidity`, `pressure`, and `wind_speed`.

## Configuration:
- **Locations**: Add or remove locations in the `locations` list within the `config` dictionary.
- **Units**: Switch between `"metric"` (Celsius) or `"imperial"` (Fahrenheit) units by changing the `units` value.
- **File Names**: Modify the `filename_json` and `filename_csv` in the `config` dictionary to customize the filenames.

## License
This project is licensed under the MIT License.
