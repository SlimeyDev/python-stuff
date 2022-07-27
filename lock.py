import datetime
import time
import os

now = datetime.datetime.now()

while True:
    if now.hour > 18 and now.hour < 7:
        os.system('shutdown -s -t 120 /c "shutting down in 2 minutes! Make sure to save your work, see ya later aligator!"')
        break
    time.sleep(.01)