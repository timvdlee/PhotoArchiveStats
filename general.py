from loadData import getData
from inventorize import ImageExifData
from collections import Counter

data = getData()

print(f"Total number of photos: {len(data)}")

print(f"Total number of photos with Exif data: {sum([1 for d in data if d.hasExif])}")

print(f"Total with GPS data: {sum([1 for d in data if d.get_GPSInfo()])}")