from libtiff import TIFF

# to open a tiff file for reading:

tif = TIFF.open(r"D:\CAMELYON16\testing\images\test_003.tif", mode='r')
print(tif)
