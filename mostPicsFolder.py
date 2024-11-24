from loadData import getData
from inventorize import ImageExifData
from collections import Counter
import calendar

data = getData()

# dates = []
# datesDict = {}

# for date in data:
#     if date.dateTime:
#         strDate = date.get_date().strftime('%Y-%m-%d')
#         dates.append(strDate)
#         if not strDate in datesDict:
#             datesDict[strDate] = [date.get_filePath()]
#         else:
#             datesDict[strDate].append(date.get_filePath())



# CounterDates = Counter(dates)


# maxDate = max(CounterDates, key=CounterDates.get)

# print(maxDate)
# print(len(datesDict["2024-11-02"]))


maps = [d.get_parentFolder() for d in data if d.get_parentFolder()]

CounterMaps = Counter(maps)

import matplotlib.pyplot as plt

# Filter maps with more than 100 counts
filtered_maps = {k: v for k, v in CounterMaps.items() if v > 100}

# Sort the filtered maps by count
sorted_maps = dict(sorted(filtered_maps.items(), key=lambda item: item[1], reverse=True))

# Plotting
plt.figure(figsize=(10, 5))
plt.barh(list(sorted_maps.keys()), list(sorted_maps.values()))
plt.title('Aantal Foto\'s per Map (Meer dan 100)', fontsize=14)
plt.xlabel('Aantal Foto\'s', fontsize=12)
plt.ylabel('Map', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

