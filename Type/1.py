
import sys

sys.path.append('E:\\Anaconda\\libs')
import numpy as np  # numpy：提供矩阵运算功能的库
import cv2  # cv2：opencv库
# -*- coding:utf-8 -*-
import os  # os：操作系统相关的信息模块

# /home/xiao...：绝对地址，/home/xiao...：相对地址；
data_base_dir = "H:\\基于CNN的图像分类\\绘画图像\\敦煌\\敦煌02"  # 存放原始图片地址
save_dir = "H:\\基于CNN的图像分类\\绘画图像\\敦煌\\02"  # 保存生成图片地址
# 存放图片名及目标区域(x,y,w,h)的txt文件地址
# 形如：000001.tif 87 90 126 160,下面只需要用到图片名，也可不写目标区域(x,y,w,h)
read_file_name_rect = "H:\\基于CNN的图像分类\\绘画图像\\敦煌\\敦煌02\\dir.txt"

# =========== read rect file ===============
with open(read_file_name_rect, "r") as ins:  # 以只读方式打开文件read_file_name_rect，并将其赋值给ins
    array_rect = []  # 定义一个空列表，读文件中每行，作为其一个元素
    for line in ins:  # 依次读ins中每个元素
        array_rect.append(line)  # 将line元素，添加到列表array_rect最后
array_rect = array_rect[1:]  # 切片，舍弃第0个，从第1个取到最后一个
number_of_lines = len(array_rect)  # 取列表长度，即列表中有多少个元素。
print("number_of_lines:", number_of_lines )
 # 输出列表元素个数

# =========== Start processing ===============
save_file_number = 0  # 定义变量，表示保存图片的个数

for current_rect in range(0, number_of_lines):  # current_rect依次取值0,1,2.....number_of_lines-1
    if current_rect % 10 == 0:  # 每10次输出一次
        print("Processing rect number " + str(current_rect))
    current_info = array_rect[current_rect].split()  # 在列表中，以空格为界，对字符串进行切片处理
    current_image_name = current_info[0]  # 图片名
    # (x,y)表示图片左上角坐标，w表示宽，h表示高
    # x = max(0, int(current_info[1]))
    # y = max(0, int(current_info[2]))
    # w = int(current_info[3])
    # h = int(current_info[4])

    if current_image_name is None:  # 检查图片名是否存在
        continue  # continue：结束本次循环，break：结束当前整个循环
    read_img_name = data_base_dir + '\\' + current_image_name  # 右边进行拼接，得到左边文件名
    if not os.path.exists(read_img_name):  # 检查文件是否存在
        continue
    img = cv2.imread(read_img_name)
    # 调用opencv读取图片
    # cropped_img = img[y : y + h, x : x + w] #取原图片(y:y+h,x:x+w)区域，作为裁剪新图片
    # 将新图片文件名和地址写入file_name中，zfill(width)，width：最后的字符串宽度
    file_name = save_dir + "\\dh2_" + str(save_file_number).zfill(4) + ".jpg"
    save_file_number += 1
    cv2.imwrite(file_name, img)  # 保存图片(cropped_img)到指定位置(file_name)</span>