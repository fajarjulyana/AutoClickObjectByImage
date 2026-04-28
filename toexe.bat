pyinstaller \
--noconfirm \
--clean \
--windowed \
--onefile \
--icon=icon.ico \
--hidden-import=cv2 \
--hidden-import=cv2.cv2 \
--hidden-import=cv2.data \
--add-data "notif.wav;." \
--add-data "iklankan.png;." \
--add-data "iklankan_sekarang.png;." \
--add-data "D:\skrip otomatis\venv\Lib\site-packages\cv2\data;cv2/data" \
guiadspro.py
