import datetime
from loadData import getData
from inventorize import ImageExifData
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

data = getData()

startDate = datetime.datetime(2024, 7, 22).date()
endDate = datetime.datetime(2024, 7, 31).date()

filteredPhotos = [photo for photo in [d for d in data if d.get_dateTime()] if startDate <= photo.get_date() <= endDate]

print(f"Number of photos taken between {startDate} and {endDate}: {len(filteredPhotos)}")

# Define time periods
time_periods = {
    'Nacht': (0, 6),
    'Ochtend': (6, 12),
    'Middag': (12, 18),
    'Avond': (18, 24)
}

# Count the number of photos per day and time period
photos_per_day_period = defaultdict(lambda: Counter())

for photo in filteredPhotos:
    date = photo.get_date()
    time = photo.get_time()
    hour = time.hour
    for period, (start_hour, end_hour) in time_periods.items():
        if start_hour <= hour < end_hour:
            photos_per_day_period[date][period] += 1
            break

# Sort the dates
sorted_dates = sorted(photos_per_day_period.keys(), reverse=True)

# Add dates to dateDesc
dateDesc = ["Rotterdam -> Parijs","Parijs","Parijs > Caen","Caen","Caen","Caen -> Mt Saint Michel","Mt Saint Michel","Mt Saint Michel & Saint Malo","Mt Saint Michel -> Parijs","Parijs -> Rotterdam"]
dateDesc = [f"{date} - {desc}" for date, desc in zip(sorted_dates, dateDesc)]

# Prepare data for plotting
periods = list(time_periods.keys())
data_for_plotting = {period: [] for period in periods}

for date in sorted_dates:
    for period in periods:
        data_for_plotting[period].append(photos_per_day_period[date][period])

# Plot the data
plt.figure(figsize=(10, 5))
left = [0] * len(sorted_dates)
for period in periods:
    plt.barh(sorted_dates, data_for_plotting[period], left=left, label=period)
    left = [i + j for i, j in zip(left, data_for_plotting[period])]

plt.ylabel('Date')
plt.xlabel('Number of Photos')
plt.title('Number of Photos Taken Per Day by Time Period')
plt.grid(True)
plt.yticks(ticks=sorted_dates, labels=dateDesc)
plt.legend()
plt.tight_layout()
plt.show()
