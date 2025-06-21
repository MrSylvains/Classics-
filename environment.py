# environment.py
class EnvironmentMonitor:
    def __init__(self):
        self.temperature = 75  # Fahrenheit
        self.humidity = 40     # percent

    def read_conditions(self):
        print(f"Temperature: {self.temperature}°F, Humidity: {self.humidity}%")
        return {
            "temperature": self.temperature,
            "humidity": self.humidity
        }
