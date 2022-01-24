import pyautogui
from time import sleep

pyautogui.pause = 3
pyautogui.press('win')
sleep(1)
pyautogui.write('Estudos.xlsx')
sleep(1)
pyautogui.press('Enter')
sleep(8)
pyautogui.click(x=883, y=571)
sleep(4)
pyautogui.click(x=249, y=307)
pyautogui.press('backspace')
pyautogui.write('python')
pyautogui.press('Enter')
pyautogui.click(x=249, y=307)
pyautogui.doubleClick(x=267, y=315)
with pyautogui.hold('ctrlleft'):
    pyautogui.press('b')
with pyautogui.hold('altleft'):
    pyautogui.press('f4')
pyautogui.alert('O programa foi encerrado')

