import subprocess
import time
from monitor_performance import start_monitoring

def run_simulation():
    # Run the NS-3 simulation
    subprocess.run(["./ns3", "run", "scratch/simulation"])

def main():

    
    # Start performance monitoring
    start_monitoring()

    # Run the NS-3 simulation
    run_simulation()

    # Wait for the simulation to complete
    time.sleep(5)  # Adjust this time according to your simulation duration

    # Notify the user
    print("Simulation and monitoring completed. Check the 'animation.xml' for visualization.")

if __name__ == "__main__":
    main()
