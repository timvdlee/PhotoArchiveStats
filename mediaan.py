from loadData import getData
from inventorize import ImageExifData
from collections import Counter

data = getData()

dateTimes = [(d.get_dateTime(),d.get_filePath()) for d in data if d.get_dateTime()]

sortedDates = sorted(dateTimes, key=lambda x: x[0])

totalS = len(sortedDates)

min = 0
Q1 = totalS*1//4
Q2 = totalS//2
Q3 = totalS*3//4
max = totalS-1

print(f"Min: {sortedDates[min][1]}")
print(f"Q1: {sortedDates[Q1][1]}")
print(f"Q2: {sortedDates[Q2][1]}")
print(f"Q3: {sortedDates[Q3][1]}")
print(f"Max: {sortedDates[max][1]}")