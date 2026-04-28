# Auto Iklan Shopee PRO

**Auto Iklan Shopee PRO** adalah alat otomasi berbasis desktop yang dirancang untuk membantu penjual mengelola promosi produk secara otomatis menggunakan teknologi *Image Recognition*. Program ini mensimulasikan gerakan manusia (human-like movement) untuk menghindari deteksi bot dan meningkatkan efisiensi operasional toko.

## ✨ Fitur Utama

* **Image-Based Automation**: Mendeteksi tombol "Iklankan" dan "Iklankan Sekarang" secara akurat menggunakan OpenCV.
* **Human-Like Movement**: Simulasi pergerakan kursor mouse yang acak dan natural.
* **Smart Logging**: Pencatatan riwayat aktivitas ke dalam file `.txt` secara otomatis.
* **Error Handling & Screenshot**: Jika tombol tidak ditemukan, sistem akan mengambil tangkapan layar (screenshot) untuk mempermudah audit.
* **Auto Refresh**: Melakukan refresh halaman (F5) secara otomatis setiap jumlah produk tertentu untuk menjaga stabilitas sesi web.
* **Estimasi Waktu**: Menampilkan waktu berjalan (*Elapsed*) dan estimasi waktu selesai berdasarkan kecepatan proses rata-rata.
* **Audio Notification**: Memberikan sinyal suara saat seluruh proses telah selesai.

---

## 🚀 Persyaratan Sistem

Pastikan Anda telah menginstal Python 3.x dan modul-modul berikut:

```bash
pip install pyautogui opencv-python pillow
```

> **Catatan**: Program ini menggunakan fitur suara Windows (`winsound`), sehingga paling optimal dijalankan di sistem operasi Windows.

---

## 📂 Struktur File

Agar program berjalan dengan lancar, pastikan file berikut berada dalam satu folder:

1.  `main.py` (Skrip utama)
2.  `iklankan.png` (Tangkapan layar tombol "Iklankan")
3.  `iklankan_sekarang.png` (Tangkapan layar tombol konfirmasi)
4.  `notif.wav` (File suara untuk notifikasi selesai)

---

## 🛠️ Cara Penggunaan

1.  **Siapkan Gambar**: Ambil screenshot kecil pada tombol "Iklankan" di browser Anda dan simpan dengan nama `iklankan.png` (pastikan resolusi layar sama saat pengambilan gambar dan saat menjalankan bot).
2.  **Jalankan Skrip**:
    ```bash
    python main.py
    ```
3.  **Konfigurasi GUI**:
    * **Jumlah Produk**: Total produk yang ingin diproses.
    * **Auto Refresh**: Frekuensi bot menekan F5 (misalnya tiap 50 produk).
    * **Delay Min/Max**: Jeda waktu acak antar klik agar terlihat natural.
4.  **Mulai**: Tekan tombol **START**, lalu buka jendela browser Shopee Seller Centre Anda dalam 3 detik.

---

## 🕹️ Kontrol GUI

* **START**: Memulai proses otomasi.
* **STOP**: Menghentikan bot sepenuhnya.
* **PAUSE**: Menghentikan bot sementara (jeda).
* **RESUME**: Melanjutkan bot dari posisi terakhir saat di-pause.

---

## ⚠️ Disclaimer

Alat ini dibuat untuk tujuan efisiensi kerja. Pengguna bertanggung jawab penuh atas penggunaan alat ini. Pastikan untuk mengatur jeda waktu (*delay*) yang wajar untuk mematuhi kebijakan platform dan menghindari pembatasan akun.

---

## 👨‍💻 Developer
* **Nama**: Fajar Julyana
* **Perusahaan**: Hurtrock Automation Tools
* **Tahun**: © 2025 — All Rights Reserved

---

### Tips Optimasi
* Gunakan browser dengan zoom 100%.
* Pastikan area tombol tidak tertutup oleh jendela lain (Pop-up atau aplikasi lain).
* Gunakan nilai `confidence=0.80` pada skrip jika tombol sulit terdeteksi karena perbedaan kontras layar.