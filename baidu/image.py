from aip import AipImageClassify
import json


""" 你的 APPID AK SK """
APP_ID = '16749409'
API_KEY = 'sU1prFpVlWVqUpuPiiT9Q9qf'
SECRET_KEY = 'prl7qlpcGgqxGKPiubY7Vqj6lOhxC3zs'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('lion.jpg')


""" 调用通用物体识别 """
result = client.advancedGeneral(image);

print(result)

with open("lion.txt", "w", encoding="utf-8") as f:
	f.write(json.dumps(result,ensure_ascii=True))


""" 调用菜品识别 """
# client.dishDetect(image);

""" 调用红酒识别 """
# client.redwine(image);

""" 调用食材识别 """
# client.ingredient(image);

""" 调用车辆识别 """
# client.carDetect(image);

""" 调用logo商标识别 """
# client.logoSearch(image);

""" 调用动物识别 """
# client.animalDetect(image);

""" 调用植物识别 """
# client.plantDetect(image);

""" 带参数调用花卉识别 """
# client.flower(image, options)

""" 调用图像主体检测 """
# client.objectDetect(image);

""" 调用地标识别 """
# client.landmark(image);

""" 调用货币识别 """
# client.currency(image);