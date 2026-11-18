




import pyautogui, pygetwindow as gw, time, ctypes

pyautogui.FAILSAFE = True

# 1. Szukamy okna Brave i wyciagamy je na wierzch
okna = [w for w in gw.getWindowsWithTitle('Brave') if w.title]
if okna:
    brave = okna[0]
    if brave.isMinimized:
        brave.restore()
    brave.maximize()
    brave.activate()
    time.sleep(2)

# 2. Odswiezamy biezaca strone, a potem wchodzimy w Twoje konto / ogloszenia
pyautogui.press('f5')
time.sleep(3)

pyautogui.click(2157, 250)    # twoje konto (50%)
time.sleep(4)                 # Czas na zaladowanie podstrony z Twoimi ogloszeniami

# 3. Sciezka promowania
pyautogui.click(2591, 1821)   # 1. Przycisk Promuj
time.sleep(3)

pyautogui.click(1225, 612)    # 2. Przycisk Mini
time.sleep(2)

pyautogui.click(1222, 1074)   # 3. Przycisk Odswiezenie 7x
time.sleep(2)

pyautogui.click(2437, 1541)   # 4. Przycisk Dodaj promowanie
time.sleep(4)

pyautogui.click(1194, 1160)   # 5. Przycisk Upowazniam OLX...
time.sleep(2)

#pyautogui.click(2529, 1242)   # 6. Przycisk Zamawiam i place

time.sleep(3)
ctypes.windll.user32.LockWorkStation()


















# import pyautogui, pygetwindow as gw, time, ctypes

# pyautogui.FAILSAFE = True

# # 1. Szukamy okna Brave i wyciagamy je na wierzch
# okna = [w for w in gw.getWindowsWithTitle('Brave') if w.title]
# if okna:
#     brave = okna[0]
#     if brave.isMinimized:
#         brave.restore()
#     brave.maximize()
#     brave.activate()
#     time.sleep(2)

# # wyswietlenie oooglozenia na OLX
# pyautogui.click(2157, 250)  # twoje konto (50%)

# # 2. Odswiezamy strone i klikamy po kolei
# pyautogui.press('f5')
# time.sleep(4)

# pyautogui.click(2591, 1821)   # 1. Przycisk Promuj
# time.sleep(3)

# pyautogui.click(1225, 612)    # 2. Przycisk Mini
# time.sleep(2)

# pyautogui.click(1222, 1074)   # 3. Przycisk Odswiezenie 7x
# time.sleep(2)

# pyautogui.click(2437, 1541)   # 4. Przycisk Dodaj promowanie
# time.sleep(4)

# pyautogui.click(1194, 1160)   # 5. Przycisk Upowazniam OLX...
# time.sleep(2)

# #pyautogui.click(2529, 1242)   # 6. Przycisk Zamawiam i place

# time.sleep(3)
# ctypes.windll.user32.LockWorkStation()
