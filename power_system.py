# power_system.py
class PowerSystem:
    def __init__(self):
        self.battery_level = 85  # percent

    def check_battery_level(self):
        print(f"Current battery level: {self.battery_level}%")
        return self.battery_level
