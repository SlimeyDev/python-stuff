from pynput import keyboard
from pynput.keyboard import Controller as KeyboardController
import time
from pynput.keyboard import Key

def send(msg):
    keyboard1 = KeyboardController()

    keyboard1.type(msg)
    time.sleep(.5)
    keyboard1.press(Key.enter)
    time.sleep(.1)
    keyboard1.release(Key.enter)


text = str(input("Type the text you want to spam: "))

loop_times = int(input("Type the number of times you want to spam the text: "))

print('-'*33)
print("Starting in 5 seconds...")
time.sleep(5)
current_time = time.strftime("%H:%M:%S", time.localtime())
print(f"Started! Time started: {current_time}")
print('-'*33)

number = 0

for i in range(loop_times):
    number = number+1
    send(str(number))
    time.sleep(.5)
    send(str(text))
    time.sleep(3)

current_time = time.strftime("%H:%M:%S", time.localtime())

print("done!")
print(f"End time: {current_time}")
print("-"*33)