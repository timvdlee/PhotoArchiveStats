from datetime import date
from loadData import getData
from inventorize import ImageExifData
from collections import Counter
from datetime import datetime, timedelta

data = getData()

hourIncluded = [d for d in data if d.dateTime]
def round_time(dt, round_to=300):
    seconds = (dt - dt.min).seconds
    rounding = (seconds + round_to / 2) // round_to * round_to
    return dt + timedelta(0, rounding - seconds, -dt.microsecond)

hourIncluded = [d for d in data if d.dateTime]
filtered_hour = [h for h in hourIncluded if 20 <= h.get_hour() < 22]
hourIncluded = [round_time(d.dateTime) for d in filtered_hour]

print(hourIncluded[0])

import matplotlib.pyplot as plt

time_counts = Counter([h.strftime("%H:%M") for h in hourIncluded])
# print(time_counts)

sorted_times = sorted(time_counts.items())

x, y = zip(*sorted_times)

plt.figure(figsize=(10, 5))
plt.bar(x, y)
plt.grid(True)
plt.title('Photos Taken Between 20:00 and 22:00 Rounded to the Nearest 5 Minutes')
plt.xlabel('Time')
plt.ylabel('Number of Photos')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()