from PIL import Image
import pytesseract
import requests
from aip import AipOcr


""" 你的 APPID AK SK """
APP_ID = '18232468'
API_KEY = 'ELwZ1cmdtZ2IFcXw1W3dEGQX'
SECRET_KEY = 'WjbQturFrdRVFjINbEsXD6Awij3ZRbpR'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

img_src = 'https://shop.suzhoubank.com/member/verificationCode/generate'


def ocr(img):
	image = Image.open(str(img) + '.jpg')
	
	width = image.size[0]   # 106
	height = image.size[1]  # 30 

	for i in range(0, width):
		for j in range(0, height):
			data = image.getpixel((i, j))
			# print(data)
			if(data[0]< 30 and data[1]< 30 and data[2]< 30):  # 去掉黑框 黑线
				image.putpixel((i,j), (255, 255, 255))
				
			# if(data[0]< 100 or data[1]< 100 or data[2]< 100):  # 去噪点
			# 	image.putpixel((i,j), (0, 0, 0))
			# else:
			# 	image.putpixel((i,j), (255, 255, 255))
	image = image.convert("L")
	image = image.point(lambda i : 255 if i > 225 else 0)
	image.save(str(img) + '.jpg')

	result = pytesseract.image_to_string(image, lang= 'lpp').replace(' ', '')
	print(result)
	image.show()


for i in range(1, 11):
	img = requests.get(img_src)
	with open(str(i) + '.jpg', 'wb') as f:
		f.write(img.content)
		f.close()
	ocr(i)
	result = client.basicGeneral(img.content)
	print(result)

