from loadData import getData
from inventorize import ImageExifData
from collections import Counter
import shutil

data = getData()

hourIncluded = [d for d in data if d.dateTime]
filtered_hour = [h for h in hourIncluded if 2 <= h.get_hour() <= 5]

hours = [(h.get_fileName(),h.get_dateTime(),h.get_filePath()) for h in filtered_hour]
for f,d,p in hours:
    print(p,d)



# for d in filtered_hour:
#     shutil.copy2(d.get_filePath(), 'Nacht/')	
