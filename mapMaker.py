import pickle
from inventorize import ImageExifData
from collections import Counter
import folium
import math
from loadData import getData



# Print the loaded data (optional)
GPS_INFO = [(d.get_GPSInfo(),d) for d in getData() if d.get_GPSInfo()]



# Create a map centered around the average coordinates
average_lat = 52.3676  # Hardcoded latitude
average_lon = 4.9041   # Hardcoded longitude
map = folium.Map(location=[average_lat, average_lon], zoom_start=10)

def dms_to_decimal(degrees, minutes, seconds):
    return degrees + (minutes / 60) + (seconds / 3600)
it = 0
# Add markers to the map
for i in GPS_INFO:
    info,obj = i
    try:
        info[2], info[4]
        lat = dms_to_decimal(*info[2])
        long = dms_to_decimal(*info[4])
        if math.isnan(lat) or math.isnan(long):
            continue
        folium.Marker(location=[lat, long],tooltip=f"{obj.get_yearFolder()}/{obj.get_parentFolder()}/{obj.get_fileName()}").add_to(map)
        it += 1
    except KeyError:
        pass
    
    print(it)

# Save the map to an HTML file
map.save('map.html')
