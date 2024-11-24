from loadData import getData
from inventorize import ImageExifData
from collections import Counter
import calendar
import matplotlib.pyplot as plt

data = getData()

dates = []
datesDict = {}

for date in data:
    if date.dateTime:
        strDate = date.get_date().strftime('%Y-%m-%d')
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


dates2 = [f"{datesDict[date][0].get_parentFolder()} - {date}" for date in dates]

# Create a dictionary to count the number of photos taken by each camera model on each date
camera_counts = {date: Counter([img.get_CameraModel() for img in datesDict[date]]) for date in dates}

# Create a list of unique camera models that occur more than 100 times
camera_model_counts = Counter(camModel)
unique_cameras = [camera for camera, count in camera_model_counts.items() if count > 67]

# Add "Misc" category for cameras that do not meet the threshold
misc_cameras = [camera for camera in camera_model_counts if camera not in unique_cameras]
unique_cameras.append('Misc')

# Sort unique_cameras based on the counts in camera_model_counts
unique_cameras.sort(key=lambda camera: camera_model_counts[camera] if camera != 'Misc' else sum(camera_model_counts[misc_camera] for misc_camera in misc_cameras), reverse=True)

# Create a color map for the camera models
color_map = plt.get_cmap('tab20', len(unique_cameras))

# Create a horizontal bar plot with stacked bars
plt.figure(figsize=(10, 8))

# Initialize the bottom position for the stacked bars
bottom = [0] * len(dates)

# Plot each camera model's contribution to the total count
for i, camera in enumerate(unique_cameras):
    if camera == 'Misc':
        camera_counts_per_date = [sum(camera_counts[date][misc_camera] for misc_camera in misc_cameras) for date in dates]
    else:
        camera_counts_per_date = [camera_counts[date][camera] for date in dates]
    plt.barh(dates2, camera_counts_per_date, left=bottom, color=color_map(i), label=camera)
    bottom = [sum(x) for x in zip(bottom, camera_counts_per_date)]

print(len(unique_cameras))

plt.xlabel('Number of Photos')
plt.ylabel('Date')
plt.grid(True)
plt.title('Top 25 Dates with the Most Photos by Camera Model')
plt.gca().invert_yaxis()  # Invert y-axis to have the date with the most photos at the top
plt.legend(title='Camera Model')
plt.show()
