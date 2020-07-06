import os
import time
from PIL import Image

os.system("adb shell screencap /sdcard/0.png")
time.sleep(1)
os.system("adb pull /sdcard/0.png .")

image = Image.open("0.png")
image.show()