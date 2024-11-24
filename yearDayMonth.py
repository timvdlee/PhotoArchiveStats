from loadData import getData
from inventorize import ImageExifData
from collections import Counter
import calendar

data = getData()

years = [d.get_yearFolder() for d in data]

year_counts = Counter(years)

print(year_counts)
import matplotlib.pyplot as plt

# Plotting the year_counts in a barplot
plt.bar(year_counts.keys(), year_counts.values())
plt.xlabel('Year')
plt.ylabel('Number of Photos')
plt.grid(True)
plt.title('Number of Photos per Year')
plt.show()


# Get the month names in Dutch
month_names_dutch = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']

# Extract months from data
months = [d.get_month() for d in data if d.get_month()]

# Count occurrences of each month
month_counts = Counter(months)

# Sort the months by their numerical value
sorted_months = sorted(month_counts.keys())

# Plotting the month_counts in a barplot
plt.bar([month_names_dutch[m-1] for m in sorted_months], [month_counts[m] for m in sorted_months])
plt.xlabel('Maand')
plt.ylabel('Aantal Foto\'s')
plt.grid(True)

plt.title('Aantal Foto\'s per Maand')
plt.show()


# Extract days from data
days = [d.get_day() for d in data if d.get_day()]

# Count occurrences of each day
day_counts = Counter(days)

# Sort the days by their numerical value
sorted_days = sorted(day_counts.keys())

# Plotting the day_counts in a barplot
plt.bar(sorted_days, [day_counts[d] for d in sorted_days])
plt.xlabel('Dag')
plt.grid(True)
plt.xticks(range(1,32))
plt.ylabel('Aantal Foto\'s')
plt.title('Aantal Foto\'s per Dag van de Maand')
plt.show()