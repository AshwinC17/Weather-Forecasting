import requests
from datetime import datetime

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,uk&appid=" + API_KEY


def parse_datetime(input_str):
    try:
        return datetime.strptime(input_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


def get_weather_data(date):
    url = BASE_URL
    response = requests.get(url)

    try:
        data = response.json()
        temperature_sum = 0
        count = 0

        for item in data["list"]:
            dt_txt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
            if date.date() == dt_txt.date():
                temperature_sum += item["main"]["temp"]
                count += 1

        if count == 0:
            return None

        average_temperature = temperature_sum / count
        return average_temperature
    except KeyError:
        return None


def get_wind_speed(date):
    url = BASE_URL
    response = requests.get(url)

    try:
        data = response.json()
        wind_speed_sum = 0
        count = 0

        for item in data["list"]:
            dt_txt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
            if date.date() == dt_txt.date():
                wind_speed_sum += item["wind"]["speed"]
                count += 1

        if count == 0:
            return None

        average_wind_speed = wind_speed_sum / count
        return average_wind_speed
    except KeyError:
        return None


def get_pressure(date):
    url = BASE_URL
    response = requests.get(url)

    try:
        data = response.json()
        pressure_sum = 0
        count = 0

        for item in data["list"]:
            dt_txt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
            if date.date() == dt_txt.date():
                pressure_sum += item["main"]["pressure"]
                count += 1

        if count == 0:
            return None

        average_pressure = pressure_sum / count
        return average_pressure
    except KeyError:
        return None


def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            date_str = input("Enter the date and time (YYYY-MM-DD HH:mm:ss): ")
            date = parse_datetime(date_str)
            if date is not None:
                temperature = get_weather_data(date)
                if temperature is not None:
                    print(f"Average temperature on {date_str}: {temperature:.2f} °K")
                else:
                    print("Data not found for the provided date.")
            else:
                print("Invalid date and time format. Please try again.")
        elif choice == 2:
            date_str = input("Enter the date and time (YYYY-MM-DD HH:mm:ss): ")
            date = parse_datetime(date_str)
            if date is not None:
                wind_speed = get_wind_speed(date)
                if wind_speed is not None:
                    print(f"Average Wind Speed on {date_str}: {wind_speed:.2f} m/s")
                else:
                    print("Data not found for the provided date.")
            else:
                print("Invalid date and time format. Please try again.")
        elif choice == 3:
            date_str = input("Enter the date and time (YYYY-MM-DD HH:mm:ss): ")
            date = parse_datetime(date_str)
            if date is not None:
                pressure = get_pressure(date)
                if pressure is not None:
                    print(f"Average Pressure on {date_str}: {pressure:.2f} hPa")
                else:
                    print("Data not found for the provided date.")
            else:
                print("Invalid date and time format. Please try again.")
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
