import pyautogui as sender
import time

limit = input("How many times do you want to send the message? ")
msg = input("What message do you want to send? ")

i = 0

time.sleep(5)

while i < int(limit):
    sender.typewrite(msg)
    sender.press("enter")
    

   