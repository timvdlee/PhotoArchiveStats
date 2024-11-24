from loadData import getData
from inventorize import ImageExifData
from collections import Counter
import matplotlib.pyplot as plt

data = getData()

# Get the parent folders
folders = [d.get_parentFolder() for d in data if d.get_parentFolder()]

# Count the occurrences of each folder
CounterMaps = Counter(folders)

# Get the most common folders and their counts
most_common_folders = CounterMaps.most_common(25)

# Separate the folders and counts for plotting
folders, counts = zip(*most_common_folders)

camModel = [d.get_CameraModel() for d in data if d.get_dateTime()]

# Create a dictionary to count the number of photos taken by each camera model in each folder
folder_counts = {folder: Counter([img.get_CameraModel() for img in data if img.get_parentFolder() == folder]) for folder in folders}

# Create a list of unique camera models that occur more than 67 times
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
bottom = [0] * len(folders)

# Plot each camera model's contribution to the total count
for i, camera in enumerate(unique_cameras):
    if camera == 'Misc':
        camera_counts_per_folder = [sum(folder_counts[folder][misc_camera] for misc_camera in misc_cameras) for folder in folders]
    else:
        camera_counts_per_folder = [folder_counts[folder][camera] for folder in folders]
    plt.barh(folders, camera_counts_per_folder, left=bottom, color=color_map(i), label=camera)
    bottom = [sum(x) for x in zip(bottom, camera_counts_per_folder)]

print(len(unique_cameras))

plt.xlabel('Number of Photos')
plt.ylabel('Folder')
plt.grid(True)
plt.title('Top 25 Folders with the Most Photos by Camera Model')
plt.gca().invert_yaxis()  # Invert y-axis to have the folder with the most photos at the top
plt.legend(title='Camera Model')
plt.show()
