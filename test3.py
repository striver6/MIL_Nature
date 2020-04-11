from osgeo import gdal
file_path="D:/work/python/Tif_to_png/a_image.tif"
ds=gdal.Open(file_path)
driver=gdal.GetDriverByName('PNG')
dst_ds = driver.CreateCopy('D:/work/python/Tif_to_png/example.png', ds)
dst_ds = None
src_ds = None