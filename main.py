import time
import threading
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController

# --- Configuration ---
SPACE_TOGGLE = Key.f8   # Press F8 to start/stop Spacebar spamming
CLICK_TOGGLE = Key.f9   # Press F9 to start/stop Mouse Clicking
DELAY = 0.05            # Time between actions (0.05 seconds = 20 times/sec)

# Controllers
mouse = MouseController()
keyboard = KeyboardController()

# Toggle States
space_running = False
click_running = False

def space_loop():
    """Background loop for spacebar pressing."""
    while True:
        if space_running:
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            time.sleep(DELAY)
        else:
            time.sleep(0.1)

def click_loop():
    """Background loop for mouse clicking."""
    while True:
        if click_running:
            mouse.click(Button.left, 1)
            time.sleep(DELAY)
        else:
            time.sleep(0.1)

def on_press(key):
    """Listens for F8 and F9 to toggle the loops."""
    global space_running, click_running
    
    if key == SPACE_TOGGLE:
        space_running = not space_running
        status = "[ACTIVE]" if space_running else "[PAUSED]"
        print(f"{status} Spacebar macro.")
        
    elif key == CLICK_TOGGLE:
        click_running = not click_running
        status = "[ACTIVE]" if click_running else "[PAUSED]"
        print(f"{status} Mouse clicker.")

# Start background threads so they run simultaneously
threading.Thread(target=space_loop, daemon=True).start()
threading.Thread(target=click_loop, daemon=True).start()

print("--- Multi-Clicker Loaded ---")
print(f"Press {SPACE_TOGGLE} to toggle Spacebar spamming.")
print(f"Press {CLICK_TOGGLE} to toggle Mouse clicking.")
print("----------------------------")

with Listener(on_press=on_press) as listener:
    listener.join()
