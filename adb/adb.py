import os
import time
from PIL import Image

def screen():
	os.system("adb shell screencap /sdcard/0.png")
	time.sleep(1)
	os.system("adb pull /sdcard/0.png .")
	image = Image.open("0.png")
	image.show()

#for i in range(10):
#	screen()

screen()