import pandas
import pyautogui
import time
import os

pyautogui.PAUSE = 0.5

source = os.path.abspath('.')
path = os.path.join(source, 'produtos.csv')

pyautogui.press("win")
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=932, y=57)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')


pyautogui.click(x=956, y=372)
pyautogui.hotkey('crtl' + 'a')
pyautogui.write('email@gmail.com')
pyautogui.press('tab')
pyautogui.hotkey('crtl' + 'a')
pyautogui.write('senha')
pyautogui.press('tab')
pyautogui.press('enter')