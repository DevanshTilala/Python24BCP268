class Weather:
    def __init__(self,temp,hum,wind,pressure):
        self.parameters=[temp,hum,wind,pressure]
    def __contains__(self,element):
        return element in self.parameters

temperature=float(input("Enter the temperature: "))
humidity=int(input("Enter the humidity: "))
wind=float(input("Enter the wind speed: "))
pressure=float(input("Enter the pressure: "))
w1=Weather(temperature,humidity,wind,pressure)
if temperature in w1:
    print("Given parameter is present")