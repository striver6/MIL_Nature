import cv2
import numpy as np
from matplotlib import pyplot as plt
import openslide



img = openslide.OpenSlide("D:/1.svs")

# global thresholding
print(type(img))
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print(ret1)
print(th1)
print(type(th1))
print(th1.shape)

# plot all the images and their histograms
images = [img, 0, th1]
titles = ['Original Noisy Image']
plt.imshow(images[0],'gray')
plt.title(titles[0]), plt.xticks([]), plt.yticks([])
plt.show()