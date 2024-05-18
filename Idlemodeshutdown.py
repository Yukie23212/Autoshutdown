import pyautogui
import time
import subprocess

def check_idle_time(timeout=3600):
    last_pos = pyautogui.position()
    last_move_time = time.time()
    while True:
        current_pos = pyautogui.position()
        if current_pos != last_pos:
            last_pos = current_pos
            last_move_time = time.time()
        elif (time.time() - last_move_time) > timeout:
            print("No mouse movement detected. Shutting down...")
            subprocess.call(["shutdown", "/s", "/t", "1"])  # Shutdown the computer
            break
        time.sleep(1)

if __name__ == "__main__":
    check_idle_time()
