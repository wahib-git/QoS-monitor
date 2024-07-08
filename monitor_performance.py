import psutil
import time
import threading

def monitor_performance():
    #while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        active_processes = len(psutil.pids())
       
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print(f"Active Processes: {active_processes}")
       

def start_monitoring():
    monitoring_thread = threading.Thread(target=monitor_performance)
    monitoring_thread.daemon = True
    monitoring_thread.start()
