import pandas
import pyautogui
import time
import os

pyautogui.PAUSE = 0.5

source = os.path.abspath('.')
path = os.path.join(source, 'produtos.csv')

tabela = pandas.read_csv(path)

pyautogui.press("win")
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=932, y=57)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')


time.sleep(3)
pyautogui.click(x=956, y=372)
pyautogui.hotkey('crtl' + 'a')
pyautogui.write('email@gmail.com')
pyautogui.press('tab')
pyautogui.hotkey('crtl' + 'a')
pyautogui.write('senha')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)



codigo = str(tabela.loc[linha, 'codigo'])
marca = str(tabela.loc[linha, 'marca'])
tipo = str(tabela.loc[linha, 'tipo'])
categoria = str(tabela.loc[linha, 'categoria'])
preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
custo = str(tabela.loc[linha, 'custo'])
obs = str(tabela.loc[linha, 'obs'])
