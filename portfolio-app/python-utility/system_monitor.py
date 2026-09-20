import shutil
import psutil
from datetime import datetime

def check_system_health():
    print("==========================================")
    print(f"System Health Audit Report: {datetime.now()}")
    print("==========================================")

    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"[INFO] CPU Usage: {cpu_usage}%")

    # Memory Usage
    memory = psutil.virtual_memory()
    print(f"[INFO] Total Memory: {memory.total / (1024**3):.2f} GB")
    print(f"[INFO] Used Memory: {memory.percent}%")

    # Disk Usage
    disk = shutil.disk_usage("/")
    disk_percent = (disk.used / disk.total) * 100
    print(f"[INFO] Total Disk Space: {disk.total / (1024**3):.2f} GB")
    print(f"[INFO] Used Disk Space: {disk_percent:.2f}%")

    # Health Status Check
    if cpu_usage > 80 or memory.percent > 80 or disk_percent > 85:
        print("[WARNING] High resource utilization detected!")
    else:
        print("[SUCCESS] All system metrics are within normal range.")
    print("==========================================")

if __name__ == "__main__":
    check_system_health()