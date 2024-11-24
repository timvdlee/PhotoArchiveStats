from datetime import date
from loadData import getData
from inventorize import ImageExifData
from collections import Counter

data = getData()

hour = [(d.get_time_hhmm(),d.get_dateTime(),d.get_filePath()) for d in data if d.dateTime]

halfTien = [d for d in hour if d[0] == "22:30"]
for i,d,v in halfTien:
    print(v,d)
    
    filtered = [d for d in hour if "22:25" <= d[0] <= "22:35"]
    for i, d, v in filtered:
        print(v, d)


