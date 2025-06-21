# main.py
from monitor import OffGridMonitor

def main():
    monitor = OffGridMonitor()
    monitor.run_monitoring_cycle()

if __name__ == "__main__":
    main()
