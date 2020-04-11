import os

import cv2
import matplotlib.pyplot as plt
import openslide
from PIL import Image
from openslide.deepzoom import DeepZoomGenerator
import numpy as np
from tqdm import trange

tile_size, overlap = 224, 0
src = r'E:\DingLian\20180803\SVSFiles'
im_path = os.path.join(src, '8602.svs')

osr = openslide.open_slide(im_path)

level = 1
image = np.asarray(osr.read_region((0, 0), level, osr.level_dimensions[level]).convert('RGB'), dtype=np.uint8)
image = image.copy()
temp = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)[..., 1]
temp = cv2.blur(temp, (100, 100))
temp = cv2.threshold(temp, 0, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# mask = np.empty_like(image, dtype=np.uint8)
# for c in range(3):
#     mask[..., c] = image[..., c] * temp

h, w = temp.shape
num_rows, num_cols = h // tile_size, w // tile_size
coordinates = []
for r in trange(num_rows):
    for c in range(num_cols):
        xmin, ymin = c * tile_size, r * tile_size
        xmax, ymax = (c + 1) * tile_size if (c + 1) * tile_size <= w else w, (r + 1) * tile_size if (r + 1) * tile_size <= h else h
        tile = temp[ymin: ymax, xmin: xmax]
        tile_height, tile_width = tile.shape
        if np.sum(tile) / (tile_height * tile_width) > 0.1:
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

# plt.imshow(mask)
# plt.axis('off')
# plt.show()
Image.fromarray(image).save('c.tif')

