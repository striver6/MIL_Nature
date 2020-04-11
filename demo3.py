#导入cv模块
import cv2 as cv
import numpy as np
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
#第二个参数是通道数和位深的参数，有四种选择，参考https://www.cnblogs.com/goushibao/p/6671079.html
img = cv.imread(r"D:/CAMELYON16/testing/images/test_003.tif",2)
print(img)
#在这里一开始我写成了img.shape（），报错因为img是一个数组不是一个函数，只有函数才可以加()表示请求执行，
#参考http://blog.csdn.net/a19990412/article/details/78283742
print(img.shape)
print (img.dtype)
print (img.min())
print (img.max())
#创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
#释放窗口
cv.destroyAllWindows()