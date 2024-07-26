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



for linha in tabela.index:
    pyautogui.click(x=937, y=260)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)
