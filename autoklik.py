import pyautogui
import time
import random

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def click_button(image, name):
    print(f"Mencari tombol {name}...")

    button = pyautogui.locateOnScreen(image, confidence=0.80)

    if button:
        x, y = pyautogui.center(button)
        pyautogui.moveTo(x, y, duration=random.uniform(0.15, 0.30))
        pyautogui.click()
        print(f"> Klik tombol {name}")
        return True
    else:
        print(f"> Tombol {name} tidak ditemukan.")
        return False


TOTAL_ITEMS = 2185
print("Mulai dalam 3 detik...")
time.sleep(3)

start_time = time.time()

for i in range(TOTAL_ITEMS):
    print(f"\n=== Produk ke-{i+1}/{TOTAL_ITEMS} ===")

    # Hitung elapsed & estimasi selesai
    elapsed = time.time() - start_time
    avg_per_item = elapsed / (i+1)
    remaining = (TOTAL_ITEMS - (i+1)) * avg_per_item

    print(f"⏱ Elapsed: {format_time(elapsed)} | "
          f"Estimasi selesai: {format_time(remaining)}")

    # 1. Klik "Iklankan"
    if click_button("iklankan.png", "Iklankan"):
        time.sleep(random.uniform(0.8, 1.6))

        # 2. Klik "Iklankan Sekarang"
        if click_button("iklankan_sekarang.png", "Iklankan Sekarang"):
            time.sleep(random.uniform(0.8, 1.6))

            # Scroll ke produk berikutnya
            pyautogui.scroll(-600)
            time.sleep(0.8)
        else:
            print("Popup tidak muncul → lanjut scroll")
            pyautogui.scroll(-600)
            time.sleep(0.8)

    else:
        print("Tidak ada tombol di layar, berhenti otomatis.")
        break

print("\n🎉 Selesai semua produk!")
