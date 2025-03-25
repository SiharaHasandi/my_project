# timer.py - A simple countdown timer

import time

def countdown(seconds):
    while seconds:
        print(f"Time left: {seconds} seconds", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up! ⏰")

if __name__ == "__main__":
    seconds = int(input("Enter countdown time in seconds: "))
    countdown(seconds)
