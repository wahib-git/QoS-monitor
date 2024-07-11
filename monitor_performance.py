import psutil
import time
import threading
import subprocess

def measure_latency(host):
    try:
        output = subprocess.check_output(["ping", "-c", "1", host], universal_newlines=True)
        for line in output.split('\n'):
            if "time=" in line:
                return float(line.split("time=")[-1].split(" ")[0])
    except subprocess.CalledProcessError as e:
        print(f"Error measuring latency: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error in measure_latency: {e}")
        return None
    return None

def monitor_performance():
    try:
        # CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        # Memory usage
        memory_usage = psutil.virtual_memory().percent
        # Active processes
        active_processes = len(psutil.pids())
        
        # Print current performance metrics
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print(f"Active Processes: {active_processes}")
        
        # Battery remaining time
        battery = psutil.sensors_battery()
        if battery:
            minutes_remaining = battery.secsleft // 60
            hours_remaining = minutes_remaining // 60
            minutes_remaining %= 60
            print(f"Battery Remaining: {hours_remaining} hours {minutes_remaining} minutes")
        else:
            print("Battery information not available")
        
        # Disk space
        disk_usage = psutil.disk_usage('/')
        free_space_gb = disk_usage.free / (2**30)  # convert bytes to gigabytes
        print(f"Free Disk Space: {free_space_gb:.2f} GB")
        
        # Latency to a mobile access point (example: smartphone)
        host = "127.0.0.1"  # Example host, change as needed
        latency_ms = measure_latency(host)
        if latency_ms is not None:
            print(f"Latency to {host}: {latency_ms} ms")
        else:
            print(f"Error: Unable to measure latency to {host}")
        
    except Exception as e:
        print(f"Unexpected error in monitor_performance: {e}")

def start_monitoring():
    monitoring_thread = threading.Thread(target=monitor_performance)
    monitoring_thread.start()

