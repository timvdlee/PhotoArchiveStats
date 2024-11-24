from enum import unique
from loadData import getData
from inventorize import ImageExifData
from collections import Counter

data = getData()



cameraModel = [d.get_CameraModel() for d in data if d.get_CameraModel()]

cameraModelCounter = Counter(cameraModel)
threshold = 20
grouped_cameraModelCounter = Counter()
for model, count in cameraModelCounter.items():
    if count < threshold:
        grouped_cameraModelCounter['overig 50>n'] += count
    else:
        grouped_cameraModelCounter[model] = count
        


cameraModelCounter = grouped_cameraModelCounter

import matplotlib.pyplot as plt

# # Extract camera models and their counts
models = list(cameraModelCounter.keys())
counts = list(cameraModelCounter.values())

print(set(models))

#Unsafe but idc
Owners = eval(open("camOwners.txt",encoding="utf-8").read())



# Sort the camera models and counts by counts in descending order
sorted_counts, sorted_models = zip(*sorted(zip(counts, models), reverse=True))

# Create a horizontal bar plot with sorted data
plt.figure(figsize=(10, 7))
plt.barh(sorted_models, sorted_counts, color='skyblue')
plt.xlabel('Number of Photos')
plt.ylabel('Camera Model')
plt.grid(True)
plt.title('Number of Photos per Camera Model')
plt.tight_layout()
plt.show()
# Create a dictionary to store the counts per owner
owner_counts = Counter()

# Sum the counts for each owner
for model, count in cameraModelCounter.items():
    owner = Owners.get(model, "Unknown")
    owner_counts[owner] += count

# Extract owners and their counts
owners = list(owner_counts.keys())
owner_photo_counts = list(owner_counts.values())

# Sort the owners and counts by counts in descending order
sorted_owner_counts, sorted_owners = zip(*sorted(zip(owner_photo_counts, owners), reverse=True))

# Create a horizontal bar plot with sorted data
plt.figure(figsize=(10, 7))
plt.barh(sorted_owners, sorted_owner_counts, color='lightcoral')
plt.xlabel('Number of Photos')
plt.ylabel('Owner')
plt.grid(True)
plt.title('Number of Photos per Owner')
plt.tight_layout()
plt.show()