import pyautogui
from virtual_assistant import desktop_assistant, speak

def screenshot():
    print(desktop_assistant + ": Hold the Screen for few seconds.let me take the screenshot")
    speak("Hold the Screen for few seconds Sir.let me take the screenshot")
    im = pyautogui.screenshot()
    im.save("screenshot.jpg")
    print(desktop_assistant + ": Screenshot successfully saved in current folder")
    speak("Screenshot successfully saved in current folder")