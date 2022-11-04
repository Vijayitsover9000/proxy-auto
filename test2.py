import pyautogui as pag   
# 👆This is a python library to for gui
import time
# 👆 This library is for time functions
time.sleep(1) 
# 👆 This is for a delay of 1 second 
print("working on it")
pag.keyDown('super')
pag.press('i')
pag.keyUp('super')

# The above three lines are to open settings as hotkey function is not working on my laptop

pag.click()
time.sleep(1)
pag.write(' proxy',interval =0.25)
pag.press('enter')
time.sleep(1)
pag.press('enter')
pag.moveTo(1600,550,0.8)
pag.click()
pag.moveTo(700,355,0.8)
time.sleep(1)
pag.click()
time.sleep(1)
pag.moveTo(800,800,0.8)
pag.click()
pag.moveTo(1900,30,0.8)
pag.click()