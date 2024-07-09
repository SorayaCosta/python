import pyautogui
import subprocess
import time

url_google_maps = "https://www.google.com/maps"

subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
time.sleep(1)
pyautogui.write(url_google_maps)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("Estacao Ipiranga")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("tab")
time.sleep(1)
pyautogui.press("tab")
time.sleep(1)
pyautogui.press("tab")
time.sleep(1)
pyautogui.press("tab")
time.sleep(1)
pyautogui.press("enter")