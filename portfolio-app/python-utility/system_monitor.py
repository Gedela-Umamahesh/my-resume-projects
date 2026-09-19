import os
import platform
import shutil
import datetime
import psutil
import socket

def print_banner():
    print("=" * 60)
    print("   ULTIMATE DEVOPS SYSTEM & TELEMETRY MONITOR   ")
    print("=" * 60)

def get_system_report():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Environment & Network Stats
    sys_name = platform.system()
    sys_release = platform.release()
    machine = platform.machine()
    processor = platform.processor()
    current_user = os.getlogin() if hasattr(os, 'getlogin') else "Unknown"
    
    # Hostname & IP Address
    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
    except Exception:
        local_ip = "Unavailable"

    # CPU & RAM Metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)
    ram = psutil.virtual_memory()
    ram_total_gb = ram.total // (2**30)
    ram_used_gb = ram.used // (2**30)
    ram_percentage = ram.percent

    # Active Processes Count
    process_count = len(psutil.pids())

    # Disk Analytics
    total, used, free = shutil.disk_usage("/")
    total_gb = total // (2**30)
    used_gb = used // (2**30)
    used_percentage = (used / total) * 100

    # Directory files count
    files = os.listdir('.')
    file_count = len(files)

    report_content = f"""
============================================================
DEVOPS INFRASTRUCTURE & TELEMETRY REPORT
Generated On: {timestamp}
============================================================
[1] HOST & ENVIRONMENT PROFILE:
    - Hostname       : {hostname}
    - Local IP       : {local_ip}
    - User Profile   : {current_user}
    - Operating Sys  : {sys_name} {sys_release} ({machine})
    - Processor Cores: {cpu_count} Logical Cores

[2] HARDWARE & PROCESS PERFORMANCE:
    - CPU Usage      : {cpu_usage}%
    - RAM Utilization: {ram_used_gb} GB / {ram_total_gb} GB ({ram_percentage}%)
    - Active Processes: {process_count} running tasks

[3] DISK STORAGE METRICS:
    - Total Capacity : {total_gb} GB
    - Used Space     : {used_gb} GB ({used_percentage:.2f}%)
    - Available Free : {free // (2**30)} GB

[4] WORKSPACE AUDIT:
    - Total Items    : {file_count}
    - Items List     : {', '.join(files)}
============================================================
Status: SUCCESS - Infrastructure metrics logged securely.
============================================================
"""
    return report_content

if __name__ == "__main__":
    print_banner()
    report = get_system_report()
    print(report)

    # Automatically save report to a log file
    log_filename = "system_report.log"
    with open(log_filename, "w") as log_file:
        log_file.write(report)
    
    print(f"[INFO] Infrastructure telemetry compiled and saved to '{log_filename}'!")
    print("=" * 60)