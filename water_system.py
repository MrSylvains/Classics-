# water_system.py
class WaterSystem:
    def __init__(self):
        self.water_level = 50  # percent

    def check_water_level(self):
        print(f"Current water level: {self.water_level}%")
        return self.water_level
