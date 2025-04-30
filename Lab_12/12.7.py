class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

today_weather = Weather(["Temperature", "Humidity", "Pressure", "Wind", "Visibility"])

if "Humidity" in today_weather:
    print("Humidity data is available.")

if "Rainfall" not in today_weather:
    print("Rainfall data is not available.")
