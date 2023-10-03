# Weather Forecast Program

This program interacts with the OpenWeatherMap API to provide hourly weather forecasts for the city of London. It allows the user to retrieve weather data, wind speed, and pressure for a specific date within the date range of 2019-03-27 19:00:00 to 2019-03-31 17:00:00.

## Requirements

- Python 3.x
- requests library (can be installed using `pip install requests`)

## How to Use

1. Clone the repository or download the code files.
2. Ensure you have Python 3.x installed on your system.
3. Install the `requests` library by running `pip install requests`.
4. Run the program using the following command:

```bash
python weather.py
```

5. The program will present you with a menu to choose from:

```
1. Get weather
2. Get Wind Speed
3. Get Pressure
0. Exit
```

6. Enter the corresponding number to select the desired option.

- If you select option 1, the program will prompt you to enter a date (YYYY-MM-DD) and display the average temperature for that date in Kelvin.

- If you select option 2, the program will prompt you to enter a date (YYYY-MM-DD) and display the average wind speed for that date in meters per second.

- If you select option 3, the program will prompt you to enter a date (YYYY-MM-DD) and display the average pressure for that date in hectopascals (hPa).

7. The program will continue to run until you select option 0 to exit.

## Note

- The program uses the OpenWeatherMap API for hourly weather forecast data for London. Please ensure you have an internet connection to fetch the data.

- The API URL used in the program is: `https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22`

- The API may not have data for some dates or times, so the program will display "Data not found for the provided date" in such cases.

- The provided API key is a sample key and may have limited access. For continuous usage or commercial applications, consider obtaining your own API key from OpenWeatherMap.

- The program is designed to be modular with functions to handle data retrieval and user input.
