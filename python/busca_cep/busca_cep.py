import pyautogui
import subprocess
import time

url_correios = "https://buscacep.com.br/"

subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
time.sleep(1)
pyautogui.write(url_correios)
time.sleep(1)
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.write("09750-901")
time.sleep(0.5)
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.press("enter")

