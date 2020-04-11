import os

import openslide
from openslide.deepzoom import DeepZoomGenerator
import numpy as np
from tqdm import trange
import pandas as pd

from skimage import io
import matplotlib as plt

# src = r'E:\temp\WORK\DATASETS\Immunohistochemical'
# im_path = os.path.join(src, '17-06837-A103.svs')
#
# osr = openslide.open_slide(im_path)
import os
os.chdir(r"D:\CAMELYON16\testing\images")
result_path = r"D:\CAMELYON16\testing\images"
osr = openslide.OpenSlide(r"D:\CAMELYON16\testing\images\1.svs")
print(osr)
print(osr.dimensions)

print(osr.properties)


# tile_size就是每一个grid/tile的边长，overlap为重叠像素，slide会生成边长为tile_size的图片
slide = DeepZoomGenerator(osr, tile_size=224, overlap=0)
# 因为osr为金字塔图像，我觉得我们应该获取金字塔底层的图像的每一个带有组织区域的grid/tile，所有我们应该获取金字塔底层的信息
# 金字塔层数共有slide.level_count，由0开始，所以最底层的索引为slide.level_count - 1
highest_level = slide.level_count - 1
# 根据level的索引，我们可以获得最底层共有cols列，rows行个grid/tile
cols, rows = slide.level_tiles[highest_level]
print(cols,rows)

tilemean = []
for c in trange(cols):
    for r in range(rows):
        # 获取相应tile的位置、维度和图片信息
        coor = slide.get_tile_coordinates(highest_level, (c, r))
        dimension = slide.get_tile_dimensions(highest_level, (c, r))
        tile = np.asarray(slide.get_tile(highest_level, (c, r)).convert('RGB'), dtype=np.uint8)
        # io.imsave((result_path, "02" + str(c) + '_' + str(r) + ".png"),tile)  # 保存图像
        tilemean.append(tile.mean())


print(tilemean)

df = pd.DataFrame(tilemean)
df.to_csv("tile.csv")
# print("coor:",coor)
# print("dimension:",dimension)
# print("tile:",tile)
print(coor)

