import time

import pyautogui
from pyautogui import Point

ticker = input("Type a ticker: ")

print(f'make sure that your browser is maximized and there is nothing but the browser on the screen')
time.sleep(7)

with open('positions.txt', 'r') as f:
    positions = f.readlines()

exec(f'searchbox_pos = {positions[0][:-1]}')
exec(f'myscript_pos = {positions[1][:-1]}')
exec(f'more_pos = {positions[2][:-1]}')
exec(f'add_alert_pos = {positions[3][:-1]}')
exec(f'create_pos = {positions[4][:-1]}')

pyautogui.moveTo(searchbox_pos.x, searchbox_pos.y, 3)
pyautogui.leftClick()
time.sleep(2)
pyautogui.write(ticker)
pyautogui.press('enter')
time.sleep(2)

pyautogui.moveTo(myscript_pos.x, myscript_pos.y, 3)
time.sleep(2)

pyautogui.moveTo(more_pos.x, more_pos.y, 3)
time.sleep(2)
pyautogui.leftClick()

pyautogui.moveTo(add_alert_pos.x, add_alert_pos.y, 3)
pyautogui.leftClick()

pyautogui.moveTo(create_pos.x, create_pos.y, 3)
pyautogui.leftClick()

