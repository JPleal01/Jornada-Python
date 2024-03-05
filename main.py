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
time.sleep(3)
pyautogui.click(x = 800, y= 463)
pyautogui.write("joaopaulo@gmail.com")
pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.press('enter')

#buscar arquivos 
time.sleep(3)



#preencher e enviar
