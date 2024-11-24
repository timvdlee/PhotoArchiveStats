from loadData import getData
from inventorize import ImageExifData
from collections import Counter

data = getData()


filterFor = "iPhone 7"

cameraModel = [i for i in [d for d in data if d.get_CameraModel()] if i.get_CameraModel() == filterFor]

print(cameraModel)