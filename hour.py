from datetime import date
from loadData import getData
from inventorize import ImageExifData
from collections import Counter

data = getData()

hour = [d.get_hour() for d in data if d.dateTime]

hourCounter = Counter(hour)

sorted_hours = sorted(hourCounter.items())

for hour, count in sorted_hours:
    print(f"Hour: {hour}, Count: {count}")
    import matplotlib.pyplot as plt

    hours, counts = zip(*sorted_hours)

    plt.bar(hours, counts)
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Photos')
    plt.title('Number of Photos Taken Each Hour')
    plt.xticks(hours)
    plt.grid(True)
    plt.show()