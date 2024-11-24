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

Owners = eval(open("camOwners.txt", encoding="utf-8").read())

# Create a dictionary to count the number of photos taken by each camera model in each folder
folder_counts = {folder: Counter([img.get_CameraModel() for img in data if img.get_parentFolder() == folder]) for folder in folders}

# Create a list of unique camera models that occur more than 67 times
camera_model_counts = Counter(camModel)
unique_cameras = [camera for camera, count in camera_model_counts.items() if count > 1]

# Add "Misc" category for cameras that do not meet the threshold
misc_cameras = [camera for camera in camera_model_counts if camera not in unique_cameras]
unique_cameras.append('Diversen')

# Map camera models to owners
camera_to_owner = {camera: Owners.get(camera, 'Anderen - Onbekend') for camera in unique_cameras}

# Aggregate counts by owner
owner_counts = {owner: Counter() for owner in set(camera_to_owner.values())}
for folder in folders:
    for camera, count in folder_counts[folder].items():
        owner = camera_to_owner.get(camera, 'Anderen - Onbekend')
        owner_counts[owner][folder] += count

# Sort owners by total number of photos
sorted_owners = sorted(owner_counts.items(), key=lambda x: sum(x[1].values()), reverse=True)

# Create a color map for the owners
color_map = plt.get_cmap('tab20', len(owner_counts))

# Create a horizontal bar plot with stacked bars
plt.figure(figsize=(14, 8))

# Initialize the bottom position for the stacked bars
bottom = [0] * len(folders)

# Plot each owner's contribution to the total count
for i, (owner, counts) in enumerate(sorted_owners):
    owner_counts_per_folder = [counts[folder] for folder in folders]
    plt.barh(folders, owner_counts_per_folder, left=bottom, color=color_map(i), label=f"{owner} ({sum(counts.values())})")
    bottom = [sum(x) for x in zip(bottom, owner_counts_per_folder)]

plt.xlabel('Aantal Foto\'s')
plt.ylabel('Map')
plt.grid(True)
plt.title('Top 25 Mappen met de Meeste Foto\'s En wie heeft ze gemaakt?')
plt.gca().invert_yaxis()  # Invert y-axis to have the folder with the most photos at the top
plt.legend(title='Camera Eigenaar')
plt.show()
