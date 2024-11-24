from turtle import distance
from loadData import getData
from inventorize import ImageExifData
from collections import Counter

data = getData()


disances = [(d.get_distance(),d.get_filePath()) for d in data if d.get_distance()]

print(max(disances,key=lambda x: x[0]))