from loadData import getData
from inventorize import ImageExifData
from collections import Counter
import matplotlib.pyplot as plt

data = getData()

# Get the dates and parent folders
dates = []
datesDict = {}

for date in data:
    if date.dateTime:
        strDate = f"{date.get_parentFolder()} - {date.get_date().strftime('%Y-%m-%d')}"
        dates.append(strDate)
        if not strDate in datesDict:
            datesDict[strDate] = [date]
        else:
            datesDict[strDate].append(date)

CounterDates = Counter(dates)

# Get the most common dates and their counts
most_common_dates = CounterDates.most_common(25)

# Separate the dates and counts for plotting
dates, counts = zip(*most_common_dates)

camModel = [d.get_CameraModel() for d in data if d.get_dateTime()]

Owners = eval(open("camOwners.txt", encoding="utf-8").read())

# Create a dictionary to count the number of photos taken by each camera model on each date
camera_counts = {date: Counter([img.get_CameraModel() for img in datesDict[date]]) for date in dates}

# Create a list of unique camera models that occur more than 67 times
camera_model_counts = Counter(camModel)
unique_cameras = [camera for camera, count in camera_model_counts.items() if count > 67]

# Add "Misc" category for cameras that do not meet the threshold
misc_cameras = [camera for camera in camera_model_counts if camera not in unique_cameras]
unique_cameras.append('Misc')

# Map camera models to owners
camera_to_owner = {camera: Owners.get(camera, 'Anderen - Onbekend') for camera in unique_cameras}

# Aggregate counts by owner
owner_counts = {owner: Counter() for owner in set(camera_to_owner.values())}
for date in dates:
    for camera, count in camera_counts[date].items():
        owner = camera_to_owner.get(camera, 'Anderen - Onbekend')
        owner_counts[owner][date] += count

# Sort owners by total number of photos
sorted_owners = sorted(owner_counts.items(), key=lambda x: sum(x[1].values()), reverse=True)

# Create a color map for the owners
color_map = plt.get_cmap('tab20', len(owner_counts))

# Create a horizontal bar plot with stacked bars
plt.figure(figsize=(14, 8))

# Initialize the bottom position for the stacked bars
bottom = [0] * len(dates)

# Plot each owner's contribution to the total count
for i, (owner, counts) in enumerate(sorted_owners):
    owner_counts_per_date = [counts[date] for date in dates]
    plt.barh(dates, owner_counts_per_date, left=bottom, color=color_map(i), label=f"{owner} ({sum(counts.values())})")
    bottom = [sum(x) for x in zip(bottom, owner_counts_per_date)]

plt.xlabel('Number of Photos')
plt.ylabel('Date')
plt.grid(True)
plt.title('Top 25 Dates with the Most Photos by Camera Owner')
plt.gca().invert_yaxis()  # Invert y-axis to have the date with the most photos at the top
plt.legend(title='Camera Owner')
plt.show()
