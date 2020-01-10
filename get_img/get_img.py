import requests

img_src = 'https://shop.suzhoubank.com/member/verificationCode/generate'
img = requests.get(img_src)

for i in range(301, 501):
	with open(str(i) + '.jpg', 'wb') as f:
		f.write(img.content)
		f.close()
	print(i)
