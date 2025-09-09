from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
print("Starting auto-walk in 3 seconds...")
time.sleep(3)
print("Holding W key... Press CTRL + C to stop.")

try:
    while True:
        keyboard.press('w')  # Hold down the 'W' key
        time.sleep(0.1)
except KeyboardInterrupt:
    keyboard.release('w')    # Release the 'W' key when stopping
    print("\nStopped auto-walk.")

