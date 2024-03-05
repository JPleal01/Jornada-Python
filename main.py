import pyautogui
import time
import pandas




pyautogui.PAUSE = 0.8
#Abrir chrome e entrar no site
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

#preencher email e senha
time.sleep(1)
pyautogui.click(x = 800, y= 463)
pyautogui.write("joaopaulo@gmail.com")
pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.press('enter')

#buscar arquivos 

tabela = pandas.read_csv("produtos.csv")
time.sleep(1)

#preencher e enviar
for linha in tabela.index:
    pyautogui.click(x=816, y=319)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')
    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    time.sleep(0.5)
    pyautogui.press("enter")
    pyautogui.scroll(5000)
