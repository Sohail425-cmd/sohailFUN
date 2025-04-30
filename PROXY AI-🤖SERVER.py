import os
import sys
import time
import random
import webbrowser
from datetime import datetime

# Your Telegram channel link
TELEGRAM_CHANNEL_LINK = "https://t.me/+Uddse9fVNuUzZGE1"

# Try importing cfonts, and install it if not present
try:
    from cfonts import render
except ImportError:
    os.system('pip install python-cfonts')
    from cfonts import render

# Render "PROXY AI - 🤖 SERVER" in hacker theme
output = render('PROXY AI - 🤖 SERVER', colors=['green'], align='center', font='block')
print(output)

# Show Telegram Join Message
print("\n\033[92m🔹 BEFORE CONNECTING, YOU MUST JOIN OUR TELEGRAM CHANNEL 🔹\033[0m")
print("\033[96m🔗 JOIN NOW: \033[93m" + TELEGRAM_CHANNEL_LINK + "\033[0m")
print("\033[92m[ CLICK THE LINK OR PRESS ENTER TO OPEN TELEGRAM ]\033[0m")

# Open Telegram link in the default web browser when user presses ENTER
input()
webbrowser.open(TELEGRAM_CHANNEL_LINK)

# Confirmation message after joining
print("\n\033[92m✅ YOU ARE CONNECTED TO PROXY AI - 🤖 SERVER SUCCESSFUL ✅\033[0m\n")

# Initialize history to keep track of previous periods and results
history = []

# Function to simulate hacking-style loading
def hacker_loading(text, duration=2):
    sys.stdout.write(f"\033[92m{text} ")
    sys.stdout.flush()
    for _ in range(duration * 5):
        sys.stdout.write(random.choice(["█", "▓", "▒", "░"]))
        sys.stdout.flush()
        time.sleep(0.2)
    print("\033[0m ✅")

def display_period_and_timer():
    last_minute = None
    remaining_seconds = 59

    # Define the pattern for SMALL and BIG
    pattern = ["SMALL", "SMALL", "BIG", "SMALL", "SMALL", "BIG", "SMALL", "BIG"]
    pattern_length = len(pattern)

    # Green background styling for terminal (ANSI escape codes)
    print("\033[40;92m")  # Black background, green text

    while True:
        now = datetime.utcnow()

        # Simulate a server connection hacking-style
        hacker_loading("[Initializing Secure Tunnel]")
        hacker_loading("[Bypassing Firewall]")
        hacker_loading("[Connecting to PROXY AI - 🤖 SERVER]")

        # Check if the minute has changed to update the period
        if now.minute != last_minute:
            last_minute = now.minute

            # Calculate total minutes since midnight
            total_minutes = now.hour * 60 + now.minute

            # Get the pattern for the current minute based on its position
            current_pattern = pattern[total_minutes % pattern_length]

            # Format the period number for the 1-minute interval
            period_1m = now.strftime("%Y%m%d") + "1000" + str(10001 + total_minutes)

            # Add the current period and result to history
            history.append((period_1m, current_pattern))
            if len(history) > 5:  # Keep only the last 5 entries for readability
                history.pop(0)

            # Display "Loading Result..." in hacker style
            hacker_loading("\n[Decoding Data Packet...]")
            time.sleep(1)
            print(f"\033[92m[PROXY AI - 🤖 SERVER CONNECTION ESTABLISHED]\033[0m")

            # Display the current period and result in a cyberpunk table
            print(f"\n\033[92m{'='*60}")
            print(f"|{'PERIOD':^28}|{'RESULT':^28}|")  # Header
            print(f"{'-'*60}")
            print(f"|{period_1m:^28}|{current_pattern:^28}|")  # Period and result
            print(f"{'='*60}\n\033[0m")

            # Display the history of periods and results in table format
            print("\033[92m[History of Results]")
            print(f"{'='*60}")
            print(f"|{'PERIOD':^28}|{'RESULT':^28}|")
            print(f"{'-'*60}")
            for period, result in history:
                print(f"|{period:^28}|{result:^28}|")
            print(f"{'='*60}\033[0m")

            # Reset the remaining seconds to 59 at the start of a new minute
            remaining_seconds = 59

        # Format the countdown timer as "xx : xx"
        formatted_time = f"{0:02} : {remaining_seconds:02}".replace("0", " ")

        # Display the countdown timer in hacker green text
        sys.stdout.write(f"\r\033[92m[Countdown Timer] TIMER: {formatted_time}\033[0m")
        sys.stdout.flush()

        # Decrease remaining seconds
        remaining_seconds -= 1

        # Reset the countdown at the end of the minute
        if remaining_seconds < 0:
            remaining_seconds = 59

        # Wait 1 second before updating again
        time.sleep(1)

# Run the function
display_period_and_timer()