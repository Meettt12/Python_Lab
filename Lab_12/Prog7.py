#Weather

class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

today_weather = Weather(["Cloudy", "Windy", "Cold", "Hot", "Rainy"])

if "Rainy" in today_weather:
    print("Humidity data is available.")

if "Cold" not in today_weather:
    print("Rainfall data is not available.")
