import random
import time
import psutil
from JARVIS_DLG_DATASET.DLG import low_b, last_low, full_battery
from JARVIS_SPEAK.speak import speak


def battery_alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            random_low = random.choice(low_b)
            speak(random_low)

        elif percent < 10:
            random_low = random.choice(last_low)
            speak(random_low)

        elif percent == 100:
            random_low = random.choice(full_battery)
            speak(random_low)
        else:
            pass

        time.sleep(1500)

def battery_alert1():
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            random_low = random.choice(low_b)
            speak(random_low)

        elif percent < 10:
            random_low = random.choice(last_low)
            speak(random_low)

        elif percent == 100:
            random_low = random.choice(full_battery)
            speak(random_low)
        else:
            speak("sir,your battery is in perfect battery level")

