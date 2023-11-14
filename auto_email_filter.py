import pyautogui
import time

#Lines 5-9 were used once to get the necessary coordinates
# print(pyautogui.position()) #Point(x=1585, y=1483) position of outlook on laptop
# print(pyautogui.position()) Point(x=612, y=1083) skip for now
# print(pyautogui.position())Point(x=1728, y=342) x button
# print(pyautogui.position()) #Point(x=225, y=313) out search bar
# print(pyautogui.position()) # first email in list position Point(x=302, y=440)

pyautogui.PAUSE = 5

unwanted_recipients = ['IC Current','SubItUp']

pyautogui.click(x=1585,y=1483)
time.sleep(20)
pyautogui.click(x=612, y=1083)
pyautogui.click(x=1728, y=342)
for recipients in unwanted_recipients:
    pyautogui.click(x=225, y=313)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(recipients)
    pyautogui.press('enter')
    pyautogui.click(x=302, y=440)
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('delete')
