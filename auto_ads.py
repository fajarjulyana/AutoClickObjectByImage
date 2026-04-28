import pyautogui
import time
import random

def click_button(image, name):
    print(f"Mencari tombol {name}...")

    # locateOnScreen mencari gambar tombol
    button = pyautogui.locateOnScreen(image, confidence=0.8)

    if button:
        x, y = pyautogui.center(button)
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.click()
        print(f"> Klik tombol {name}")
        return True
    else:
        print(f"> Tombol {name} tidak ditemukan.")
        return False

print("Mulai dalam 3 detik...")
time.sleep(3)

for i in range(50):  # jumlah produk yang diproses
    print(f"\n=== Produk ke-{i+1} ===")

    # 1. Klik tombol Iklankan
    if click_button("iklankan.png", "Iklankan"):
        time.sleep(random.uniform(1.0, 2.0))

        # 2. Klik tombol Iklankan Sekarang
        if click_button("iklankan_sekarang.png", "Iklankan Sekarang"):
            time.sleep(random.uniform(1.0, 2.0))

            # Scroll untuk produk berikutnya
            pyautogui.scroll(-600)
            time.sleep(1)
        else:
            print("Popup tidak muncul → lanjut scroll")
            pyautogui.scroll(-600)
            time.sleep(1)

    else:
        print("Tidak ada tombol di layar, berhenti.")
        break

print("\nSelesai!")

