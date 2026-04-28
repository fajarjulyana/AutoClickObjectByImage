import tkinter as tk
from tkinter import ttk
import threading
import time
import random
import pyautogui
import cv2
import cv2.data
import winsound
from datetime import datetime
from PIL import ImageGrab
import sys, os

def resource_path(filename):
    """Mendapatkan path file yang benar untuk PyInstaller Onefile/Onedir"""
    if hasattr(sys, '_MEIPASS'):  # Jika running dari EXE onefile
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)

running = False
pause_flag = False
log_file = f"log_autoiklan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"


# ---------------------- UTIL & HELPER ------------------------

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def log(text):
    log_box.insert(tk.END, text + "\n")
    log_box.see(tk.END)
    with open(log_file, "a") as f:
        f.write(text + "\n")

def screenshot_error(name):
    filename = f"error_{name}_{datetime.now().strftime('%H%M%S')}.png"
    img = ImageGrab.grab()
    img.save(filename)
    log(f"[!] Screenshot disimpan: {filename}")

def random_human_movement():
    pyautogui.moveRel(random.randint(-5, 5),
                      random.randint(-5, 5),
                      duration=random.uniform(0.05, 0.15))

def click_button(image, name):
    log(f"Mencari tombol {name}...")

    try:
        button = pyautogui.locateOnScreen(image, confidence=0.80)
    except Exception:
        log("[ERROR] OpenCV required: pip install opencv-python")
        return False

    if button:
        x, y = pyautogui.center(button)
        random_human_movement()
        pyautogui.moveTo(x, y, duration=random.uniform(0.15, 0.35))
        pyautogui.click()
        log(f"> Klik tombol {name}")
        return True
    else:
        log(f"> Tidak ditemukan: {name}")
        return False

# ---------------------- NOTIFIKASI ------------------------

def play_notif():
    winsound.PlaySound("notif.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)


# ---------------------- THREAD UTAMA ------------------------

def automation_thread():
    global running, pause_flag
    running = True
    pause_flag = False

    total_items = int(entry_jumlah.get())
    refresh_every = int(entry_refresh.get())
    delay_min = float(entry_delay_min.get())
    delay_max = float(entry_delay_max.get())

    time_history = []
    start_time = time.time()

    log("Mulai dalam 3 detik...")
    time.sleep(3)

    not_found_counter = 0

    for i in range(total_items):

        if not running:
            log("=== BOT DIHENTIKAN ===")
            break

        while pause_flag:
            time.sleep(1)
            log("|| Auto Paused — menunggu Resume ||")
            continue

        log(f"\n=== Produk ke-{i+1}/{total_items} ===")

        # Moving average untuk estimasi
        elapsed = time.time() - start_time
        time_history.append(elapsed / (i+1))
        if len(time_history) > 20:
            time_history.pop(0)

        avg = sum(time_history) / len(time_history)
        remaining = (total_items - (i+1)) * avg

        label_elapsed.config(text=f"Elapsed: {format_time(elapsed)}")
        label_estimate.config(text=f"Estimasi selesai: {format_time(remaining)}")
        progress['value'] = ((i+1) / total_items) * 100

        # ----------- Refresh otomatis ---------
        if (i > 0) and (i % refresh_every == 0):
            log(" AUTO REFRESH PAGE")
            pyautogui.press("f5")
            time.sleep(5)

        # ----------- Klik tombol utama ---------
        if click_button("iklankan.png", "Iklankan"):

            time.sleep(random.uniform(delay_min, delay_max))

            if click_button("iklankan_sekarang.png", "Iklankan Sekarang"):
                pyautogui.scroll(-300)
                time.sleep(random.uniform(delay_min, delay_max))
            else:
                log("Popup tidak muncul — AUTO SKIP")
                pyautogui.scroll(-300)
                time.sleep(random.uniform(0.5, 1.0))

            not_found_counter = 0

        else:
            not_found_counter += 1
            screenshot_error("notfound")

            if not_found_counter >= 3:
                log("=== PAUSE: Tombol tidak ditemukan 3x ===")
                pause_flag = True

            continue

        time.sleep(random.uniform(delay_min, delay_max))

    play_notif()
    log("SELESAI! Semua produk selesai diproses.")
    running = False


# ---------------------- GUI CONTROL ------------------------

def start_bot():
    if running:
        return
    t = threading.Thread(target=automation_thread)
    t.daemon = True
    t.start()

def stop_bot():
    global running
    running = False
    log("Menghentikan automation...")

def pause_bot():
    global pause_flag
    pause_flag = True
    log("|| BOT DI-PAUSE ||")

def resume_bot():
    global pause_flag
    pause_flag = False
    log(">> Resume berjalan <<")

# ---------------------- GUI ------------------------

root = tk.Tk()
root.title("Auto Iklan Shopee PRO")
root.geometry("550x700")

# Input jumlah item
tk.Label(root, text="Jumlah Produk:").pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.insert(0, "2185")
entry_jumlah.pack()

# Refresh setiap
tk.Label(root, text="Auto Refresh setiap (produk):").pack()
entry_refresh = tk.Entry(root)
entry_refresh.insert(0, "50")
entry_refresh.pack()

# Delay min/max
tk.Label(root, text="Delay Min (detik):").pack()
entry_delay_min = tk.Entry(root)
entry_delay_min.insert(0, "0.8")
entry_delay_min.pack()

tk.Label(root, text="Delay Max (detik):").pack()
entry_delay_max = tk.Entry(root)
entry_delay_max.insert(0, "1.8")
entry_delay_max.pack()

# Tombol Start Stop Pause Resume
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="START", width=10, bg="green",
          fg="white", command=start_bot).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="STOP", width=10, bg="red",
          fg="white", command=stop_bot).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="PAUSE", width=10, bg="orange",
          fg="white", command=pause_bot).pack(side=tk.LEFT, padx=5)

tk.Button(frame_btn, text="RESUME", width=10, bg="blue",
          fg="white", command=resume_bot).pack(side=tk.LEFT, padx=5)

# Label waktu
label_elapsed = tk.Label(root, text="Elapsed: 00:00:00")
label_elapsed.pack()

label_estimate = tk.Label(root, text="Estimasi selesai: 00:00:00")
label_estimate.pack()

# Progress bar
progress = ttk.Progressbar(root, length=400)
progress.pack(pady=10)

# Log box
log_box = tk.Text(root, height=23)
log_box.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# ---------------------- MENU ABOUT ------------------------

def show_about():
    about_win = tk.Toplevel(root)
    about_win.title("About Auto Iklan Shopee PRO")
    about_win.geometry("350x250")
    about_win.resizable(False, False)

    tk.Label(about_win, text="Auto Iklan Shopee PRO", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(about_win, text="Developer: Fajar Julyana", font=("Arial", 11)).pack()
    tk.Label(about_win, text="© 2025 — All Rights Reserved", font=("Arial", 10)).pack()
    tk.Label(about_win, text="Hurtrock Automation Tools", font=("Arial", 10, "italic")).pack(pady=5)

    tk.Label(about_win, text="\nBuilt with Python, Tkinter & PyAutoGUI.\n",
             font=("Arial", 9)).pack()

    tk.Label(about_win, text="Include:", font=("Arial", 10, "bold")).pack()
    tk.Label(about_win, text="• Icon PNG\n• notif.wav\n• venv modules", font=("Arial", 9)).pack()

    tk.Button(about_win, text="OK", width=10, command=about_win.destroy).pack(pady=15)

# Menu bar
menubar = tk.Menu(root)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

root.mainloop()
