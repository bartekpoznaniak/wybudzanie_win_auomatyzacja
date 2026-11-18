import pyautogui, keyboard, time

with open("punkty.txt", "w", encoding="utf-8") as f:
    print("Najedz myszka na przycisk i wcisnij F8 (ESC konczy):")
    while not keyboard.is_pressed("esc"):
        if keyboard.is_pressed("f8"):
            p = pyautogui.position()
            print(f"\nZlapano ({p.x}, {p.y})")
            opis = input("Wpisz opis tego punktu: ")
            f.write(f"({p.x}, {p.y}),  # {opis}\n")
            f.flush()
            print("Zapisano! Najedz na kolejny przycisk i wcisnij F8 (lub ESC aby zakonczyc)...")
            time.sleep(0.4)
        time.sleep(0.05)

print("\nGotowe! Wszystko zapisane w pliku punkty.txt")
