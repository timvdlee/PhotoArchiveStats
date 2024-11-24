import exif
from matplotlib import artist
from loadData import getData
from inventorize import ImageExifData
from collections import Counter
from PIL import Image
import PIL.ExifTags



img = Image.open("Nacht\_MG_6862.jpg")
exif_data = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
        }

for i in exif_data:
    print(i,exif_data[i])