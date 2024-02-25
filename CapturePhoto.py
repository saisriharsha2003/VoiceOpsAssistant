import pyautogui
from virtual_assistant import desktop_assistant, user, speak

def capture_photo():
    print(desktop_assistant + ": Sure! wait a while")
    speak("Sure Sir! wait a while")
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    print(desktop_assistant + ": Smile Please")
    speak("Smile Please")
    pyautogui.press("enter")