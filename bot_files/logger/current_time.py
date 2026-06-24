from datetime import datetime

def log_time(message):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] {message}")

