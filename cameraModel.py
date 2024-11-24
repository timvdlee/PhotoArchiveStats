from loadData import getData
from inventorize import ImageExifData
from collections import Counter

data = getData()



cameraModel = [d.get_CameraModel() for d in data if d.get_CameraModel()]
cameraModelCounter = Counter(cameraModel)
# Group camera models with less than 25 counts into 'overig'
threshold = 50
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