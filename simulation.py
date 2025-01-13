import random
import time
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
import logging

keyboard_controller = KeyboardController()
mouse_controller = MouseController()

def simulate_keystrokes_and_mouse(keys, delay, should_continue):
    while should_continue():
        key = random.choice(keys)
        message = f"Simulated key: {key}"
        print(message)
        logging.info(message)
        keyboard_controller.press(key)
        keyboard_controller.release(key)
        time.sleep(delay)
        # Simulate spacebar key
        message = "Simulated key: space"
        print(message)
        logging.info(message)
        keyboard_controller.press(' ')
        keyboard_controller.release(' ')
        time.sleep(delay)
        # Simulate random mouse movement
        mouse_move = (random.randint(-50, 50), random.randint(-50, 50))
        message = f"Simulated mouse movement by: {mouse_move}"
        print(message)
        logging.info(message)
        mouse_controller.move(mouse_move[0], mouse_move[1])
        time.sleep(delay)