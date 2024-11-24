import exif
from matplotlib import artist
from loadData import getData
from inventorize import ImageExifData
from collections import Counter
from PIL import Image
import PIL.ExifTags



img = Image.open("SleutelstamFotoArchief/2022-2023/[2023.07.x] - Zomerkamp Balkan/20230720_095521.jpg")
exif_data = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
        }

for i in exif_data:
    print(i,exif_data[i])