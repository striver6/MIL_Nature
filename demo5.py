import cv2 as cv
import openslide

slide = openslide.OpenSlide(r"D:\CAMELYON16\testing\images\1.svs")

img = cv.imread('D:/训练营/深度学习/1.jpg')  # 读取图像（BGR）
# img = openslide.OpenSlide(r"D:\CAMELYON16\testing\images\1.svs")
print(type(img))

# print(slide)
# print(slide.dimensions)
#
# print(slide.properties)
