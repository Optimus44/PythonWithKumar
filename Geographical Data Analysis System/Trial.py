from geo_analysis.DataHandling import search_location
from geo_analysis.Insights import furthest_distance
from geo_analysis.Filtering import filter_by_region

locations = [
    {"id": "L001", "name": "Kigali", "region": "Central", "coordinates": (-1.9706, 30.1044)},
    {"id": "L002", "name": "Butare", "region": "Southern", "coordinates": (-2.6013, 29.7494)},
    {"id": "L003", "name": "Musanze", "region": "Northern", "coordinates": (-1.5021, 29.6831)},
    {"id": "L004", "name": "Rubavu", "region": "Western", "coordinates": (-1.6872, 29.3737)},
    {"id": "L005", "name": "Nyamata", "region": "Eastern", "coordinates": (-2.0145, 30.2653)},
    {"id": "L006", "name": "Huye", "region": "Southern", "coordinates": (-2.9205, 29.7464)},
    {"id": "L007", "name": "Gisenyi", "region": "Western", "coordinates": (-1.6969, 29.2401)},
    {"id": "L008", "name": "Kayonza", "region": "Eastern", "coordinates": (-1.6597, 30.4953)},
    {"id": "L009", "name": "Ruhengeri", "region": "Northern", "coordinates": (-1.4975, 29.6783)},
    {"id": "L010", "name": "Gicumbi", "region": "Northern", "coordinates": (-1.6549, 29.8119)}
]

# location_id = input("Enter a Location ID:")
#
# print(search_location(locations, location_id))

region = 'Northern'
filter_list = filter_by_region(locations, region)


print(furthest_distance(filter_list))

