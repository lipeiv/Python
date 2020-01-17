from PIL import Image, ImageFilter, ImageEnhance, ImageOps

# 读取图像
img = Image.open('a.png')
# 查看图像的基本信息
print((img.format, img.size, img.mode))

# 1. 图像转换为灰度图像
img1 = img.convert("L")
# img1.show()    # 显示图像

# 2. 将灰度图像转换为黑白图像，即二值化图像。
像素点的值大于某个值的时候设置为白色，小于某个值的时候设置为黑色
img2 = img1.point(lambda i: 255 if i > 252 else 0)

# 3. 反转图像，一般只对灰度图像做（255->0, 0->255, 128->127）
img3 = img1.point(lambda i: 255 - i)

# 4. 大小缩放：resize
img4 = img.resize((1024, 700))
img5 = img.resize((32, 32))

# 5. 图像的旋转
# 30度表示逆时针旋转30度，负值表示顺时针旋转
# expand: 旋转之后的图像大小是否发生变化，设置为True，表示变化，
并且对于多余的位置使用fillcolor给定的颜色填充，默认为False，表示截断
img6 = img.rotate(30, expand=True, fillcolor=(255, 255, 255))

# 6. 转置(左右内容或者上下的内容调换)
img7 = img.transpose(Image.FLIP_TOP_BOTTOM)
# 注意：旋转180度和上下转置是不同的，转置前后的图像是关于某个轴对称的。

# 7. 裁切
# box：(left, upper, right, lower)也就是一个矩行的左上角和右下角的像素点的坐标
box = (200, 80, 380, 225)  # 左上角为坐标原点
img8 = img.crop(box)

# 8. 图像的分裂和组合
r, g, b = img8.split()     # r，g，b是像素值
img9 = Image.merge('RGB', (b, g, r))

# 9. 粘贴
img10 = img.copy()
img10.paste(img9, box)

# 10. 数据增强
# 方式一：使用point对像素点的值进行操作
img11 = img.point(lambda i: i * 1.5)

# 方式二：直接分裂像素值，然后分别对不同通道的像素点进行处理
r, g, b = img.split()
r = r.point(lambda i: i * 1.2)
g = g.point(lambda i: i * 1.0 if i == 255 else i * 0.5)
img12 = Image.merge(img.mode, (r, g, b))

# 方式三：直接使用PIL中的API做数据增强
# https://pillow.readthedocs.io/en/5.2.x/reference/ImageEnhance.html
# 平衡度、亮度、对比度、清晰度....
enhance = ImageEnhance.Contrast(img)    # Contrast是对比度
img13 = enhance.enhance(factor=1.5)     # factor>1 表示加强
img13.show()