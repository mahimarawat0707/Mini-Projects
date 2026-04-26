import time
import psutil
import win32gui
import win32process
from collections import defaultdict

usage_time = defaultdict(int)

def get_active_window_process():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        process = psutil.Process(pid)
        process_name = process.name()

        window_title = win32gui.GetWindowText(hwnd)

        return f"{process_name} - {window_title}"
    except:
        return "Unknown"

print("Tracking app usage... Press Ctrl + C to stop.\n")

try:
    last_app = get_active_window_process()
    start_time = time.time()

    while True:
        time.sleep(1)

        current_app = get_active_window_process()

        if current_app != last_app:
            end_time = time.time()
            used_seconds = int(end_time - start_time)

            usage_time[last_app] += used_seconds

            print("\n========== App Usage Report ==========")
            for app, seconds in sorted(usage_time.items(), key=lambda x: x[1], reverse=True):
                mins = seconds // 60
                secs = seconds % 60
                print(f"{app} --> {mins} min {secs} sec")

            print("======================================\n")

            last_app = current_app
            start_time = time.time()

except KeyboardInterrupt:
    print("\nFinal Usage Report:\n")

    for app, seconds in sorted(usage_time.items(), key=lambda x: x[1], reverse=True):
        mins = seconds // 60
        secs = seconds % 60
        print(f"{app} --> {mins} min {secs} sec")

    print("\nTracking stopped.")
