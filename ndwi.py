'''
This script is written based on Landsat 8 data (OLI).
b2, b5 represents sequentially GREEN and SWIR.
All given paths are pre-defined, to make this program exicute, need to change path for source and destination
This code was written based on rasterio documentation and few live effective examples from Open Source community.
'''

## IMPORT LIBRARY
import rasterio
import numpy

# LOAD BANDS WITH RASTERIO
with rasterio.open('/home/saikat/Desktop/*B3.TIF') as src:
    b2 = src.read(1)
with rasterio.open('/home/saikat/Desktop/*B6.TIF') as src:
    b5 = src.read(1)

# Ignore Zero
numpy.seterr(divide='ignore', invalid='ignore')

# Calculate NDVI
ndvi = (b4.astype(float) - b3.astype(float)) / (b4 + b3)

# Define spatial characteristics of output object (basically they are analog to the input)
kwargs = src.meta
kwargs.update(dtype=rasterio.float32, count = 1)
print kwargs

# Calculate MNDWI
mndwi = (b2.astype(float) - b5.astype(float)) / (b2 + b5)
with rasterio.open('/home/saikat/Desktop/mndwi.tif', 'w', **kwargs) as dst_2:
    dst_2.write(mndwi.astype(rasterio.float32), 1)
print "COMPLETED MNDWI... FILE STORED"

