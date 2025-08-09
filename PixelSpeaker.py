import pyautogui
import time

# === CONFIG ===
arrow_pixel_pos = (137, 1024)  # Replace with your player arrow's screen position
check_interval = 0.1  # Seconds between checks

seen_colors = set()

try:
    while True:
        r, g, b = pyautogui.pixel(*arrow_pixel_pos)
        color = (r, g, b)

        if color not in seen_colors:
            seen_colors.add(color)
            print(color)

        time.sleep(check_interval)
except KeyboardInterrupt:
    print("Stopped.")
