import tkinter as tk
from tkinter import ttk
import threading
import time
import random
import pyautogui

# -------------------------
# Fungsi format waktu HH:MM:SS
# -------------------------
def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

# -------------------------
# Fungsi klik tombol via PyAutoGUI
# -------------------------
def click_button(image, name):
    log(f"Mencari tombol {name}...")

    try:
        button = pyautogui.locateOnScreen(image, confidence=0.80)
    except:
        log("ERROR: OpenCV belum terinstall. Jalankan:")
        log("pip install opencv-python")
        return False

    if button:
        x, y = pyautogui.center(button)
        pyautogui.moveTo(x, y, duration=random.uniform(0.15, 0.30))
        pyautogui.click()
        log(f"> Klik tombol {name}")
        return True
    else:
        log(f"> Tombol {name} tidak ditemukan.")
        return False


# -------------------------
# Logging ke GUI
# -------------------------
def log(text):
    log_box.insert(tk.END, text + "\n")
    log_box.see(tk.END)


# -------------------------
# Thread utama automation
# -------------------------
running = False

def automation_thread():
    global running
    running = True

    total_items = int(entry_jumlah.get())
    start_time = time.time()

    log("Mulai dalam 3 detik...")
    time.sleep(3)

    for i in range(total_items):
        if not running:
            log("=== Dihentikan oleh user ===")
            break

        log(f"\n=== Produk ke-{i+1}/{total_items} ===")

        # Hitung waktu dan estimasi
        elapsed = time.time() - start_time
        avg = elapsed / (i + 1)
        remaining = (total_items - (i + 1)) * avg

        label_elapsed.config(text=f"Elapsed: {format_time(elapsed)}")
        label_estimate.config(text=f"Estimasi selesai: {format_time(remaining)}")
        progress['value'] = ((i+1) / total_items) * 100

        # Klik tombol "Iklankan"
        if click_button("iklankan.png", "Iklankan"):
            time.sleep(random.uniform(0.8, 1.6))

            # Klik tombol popup
            if click_button("iklankan_sekarang.png", "Iklankan Sekarang"):
                time.sleep(random.uniform(0.8, 1.6))
                pyautogui.scroll(-600)
            else:
                log("Popup tidak muncul → lanjut scroll")
                pyautogui.scroll(-600)

            time.sleep(0.8)

        else:
            log("Tidak ada tombol ditemukan, automation berhenti.")
            break

    log("\n🎉 Selesai!")
    running = False


# -------------------------
# Fungsi tombol GUI
# -------------------------
def start_bot():
    if running:
        return
    t = threading.Thread(target=automation_thread)
    t.daemon = True
    t.start()

def stop_bot():
    global running
    running = False
    log("Menghentikan proses...")


# -------------------------
# GUI TKINTER
# -------------------------
root = tk.Tk()
root.title("Auto Iklan Shopee - PyAutoGUI")
root.geometry("500x600")

# Input jumlah produk
tk.Label(root, text="Jumlah Produk:").pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.insert(0, "2185")
entry_jumlah.pack()

# Tombol Start & Stop
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="START", width=10, bg="green", fg="white",
          command=start_bot).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="STOP", width=10, bg="red", fg="white",
          command=stop_bot).pack(side=tk.LEFT, padx=5)

# Info waktu
label_elapsed = tk.Label(root, text="Elapsed: 00:00:00")
label_elapsed.pack()

label_estimate = tk.Label(root, text="Estimasi selesai: 00:00:00")
label_estimate.pack()

# Progress bar
progress = ttk.Progressbar(root, length=300)
progress.pack(pady=10)

# Log box
log_box = tk.Text(root, height=20)
log_box.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

root.mainloop()
