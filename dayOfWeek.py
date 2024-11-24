from loadData import getData
from inventorize import ImageExifData
from collections import Counter

data = getData()

dayOfWeek = [d.get_dayOfWeek() for d in data if d.get_dayOfWeek()]

dayOfWeekCounter = Counter(dayOfWeek)

import matplotlib.pyplot as plt

# Print results
print(dayOfWeekCounter)
# Sort days of the week
ordered_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dayOfWeekCounter = {day: dayOfWeekCounter.get(day, 0) for day in ordered_days}
# Plot results
days = list(dayOfWeekCounter.keys())
counts = list(dayOfWeekCounter.values())

plt.bar(days, counts)
plt.xlabel('Dag van de Week')
plt.ylabel('Aantal Foto\'s')
plt.title('Aantal Foto\'s Gemaakt op Elke Dag van de Week')
plt.show()