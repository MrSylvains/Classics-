# monitor.py
from power_system import PowerSystem
from water_system import WaterSystem
from environment import EnvironmentMonitor
from utils.alerts import send_alert

class OffGridMonitor:
    def __init__(self):
        self.power = PowerSystem()
        self.water = WaterSystem()
        self.environment = EnvironmentMonitor()

    def run_monitoring_cycle(self):
        print("Running system checks...")
        power_status = self.power.check_battery_level()
        water_status = self.water.check_water_level()
        env_status = self.environment.read_conditions()

        if power_status < 20:
            send_alert("Power level critical: {}%".format(power_status))
        if water_status < 15:
            send_alert("Water tank low: {}%".format(water_status))
        if env_status['temperature'] > 90:
            send_alert("High temperature warning: {}°F".format(env_status['temperature']))

        print("Monitoring complete.")
