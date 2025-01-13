import os
import logging
from datetime import datetime
from pynput import keyboard, mouse
import time
import threading
from simulation import simulate_keystrokes_and_mouse

# Ensure the log directory exists
log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure logging with a new file for each run
log_filename = os.path.join(log_directory, datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.log')
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')

# Global variables to track last activity and simulation state
last_activity_time = time.time()
simulate = True  # Flag to determine if simulation is running
simulation_thread = None  # Thread for simulation
stop_event = threading.Event()  # Event to stop the simulation thread
is_simulating = False  # Flag to indicate if simulation is running

def on_keyboard_activity(key, button=None, pressed=None):
    global last_activity_time, simulate
    if not is_simulating:  # Ignore simulated input
        message = ""
        if button and pressed is not None:
            message = f"Real keyboard activity detected! {'Pressed' if pressed else 'Released'} {key}"
        print(message)
        logging.info(message)
    last_activity_time = time.time()

def on_keyboard_release(key):
    pass

def on_mouse_activity(x, y, button=None, pressed=None):
    global last_activity_time, simulate
    if button == mouse.Button.middle and pressed:
        simulate = False  # Stop simulation
        stop_event.set()  # Signal the simulation thread to stop
        message = "Middle mouse button clicked. Stopping simulation."
        print(message)
        logging.info(message)
    elif not is_simulating:  # Ignore simulated input
        last_activity_time = time.time()
        simulate = False  # Stop simulation if user input is detected
        stop_event.set()  # Signal the simulation thread to stop
        if button and pressed is not None:
            message = f"Real mouse click detected: {'Pressed' if pressed else 'Released'} {button}"
        else:
            message = f"Real mouse movement detected! ({x}, {y})"
        print(message)
        logging.info(message)

def monitor_activity():
    """Monitor keyboard and mouse activity."""
    with keyboard.Listener(on_press=on_keyboard_activity, on_release=on_keyboard_release) as kl, mouse.Listener(on_move=on_mouse_activity, on_click=on_mouse_activity) as ml:
        kl.join()
        ml.join()

def start_simulation(keys, delay):
    global last_activity_time, simulate, simulation_thread, is_simulating
    while True:
        if time.time() - last_activity_time >= inactivity_timeout:
            message = "Inactivity detected. Simulating keystrokes/mouse movement..."
            print(message)
            logging.info(message)
            simulate = True  # Mark simulation start
            stop_event.clear()  # Clear the stop event before starting the simulation
            is_simulating = True  # Set the flag to indicate simulation is running
            simulation_thread = threading.Thread(target=simulate_keystrokes_and_mouse, args=(keys, delay, lambda: simulate))
            simulation_thread.start()
            simulation_thread.join()  # Wait for the simulation thread to finish
            is_simulating = False  # Reset the flag after simulation
            last_activity_time = time.time()  # Reset activity timer after simulating
        time.sleep(1)  # Check for inactivity every second

if __name__ == "__main__":
    # Configuration
    keys_to_simulate = ['w', 'a', 's', 'd']  # Keys to randomly pick from
    delay_between_actions = 0.5               # Seconds between each simulated action
    inactivity_timeout = 0.5 * 60            # 30 seconds of inactivity to trigger the simulation

    # Run activity monitoring in a separate thread
    threading.Thread(target=monitor_activity, daemon=True).start()

    # Start the simulation in the main thread
    start_simulation(keys_to_simulate, delay_between_actions)