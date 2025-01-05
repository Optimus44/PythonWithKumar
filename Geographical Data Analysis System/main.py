from geo_analysis.DataHandling import search_location, view_locations, view_one_location
from geo_analysis.Filtering import filter_by_region
from geo_analysis.Insights import furthest_distance, calculate_distance

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

print("""
The Menu:
    1. View Location Data
    2. Filter Locations by Region
    3. Calculate Distance Between Locations
    4. Generate Region Insights
    5. Search Locations
    6. Exit
""")

try:
    choice = int(input("Enter Your Choice: "))

    while choice != 6:

        # View Location
        if choice == 1:
            print("Location Data: \n")
            view_locations(locations)


        # Filter Locations by Region
        elif choice == 2:
            region = input("Enter the Region to Filter (Northern, Southern, Eastern, Western): ")
            filtered_list = filter_by_region(locations, region)

            if filtered_list:
                print(f"\n{len(filtered_list)} locations found: ")
                view_locations(filtered_list)
            else:
                print("\n Region Not Found!")


        # Calculate Distance Between Locations
        elif choice == 3:
            print("Calculate Distance")
            location_1 = input("Enter the First Location ID: ")
            location_2 = input("Enter the Second Location ID: ")

            # Search for the locations - returns NONE if no found.
            first_location = search_location(locations, location_1)
            second_location = search_location(locations, location_2)

            # Check if the locations are found, both of them.
            if first_location and second_location:
                # Get the coordinates
                point_a = first_location['coordinates']
                point_b = second_location['coordinates']
                print(f"Distance between {first_location['name']} and {second_location['name']} is {calculate_distance(point_a, point_b):.2f} km")

            else:
                # Check which location not found to provide a specific message to the user:
                if not first_location and second_location:  # First location not found
                    print(f"Location with ID: {location_1} was not found")

                elif first_location and not second_location:  # Second location not found
                    print(f"Location with ID: {location_2} was not found")

                else:
                    print(f"Locations '{location_1}' and '{location_2}' were not found")


        # Generate Region Insights
        elif choice == 4:
            # Enter a region and display total locations and the furthest distance in the region.
            print("Generate Region Insights")
            region = input("Enter Your Region: ")
            print("Region: ", region)
            region_locations = filter_by_region(locations, region)
            if region_locations:
                print(f"\nTotal Locations: {len(region_locations)}.") # Total Regions
                farthest, location1, location2 = furthest_distance(region_locations)  # Tuple unpacking.
                print(f"Farthest Locations: {location1['name']} and {location2['name']} (Distance: {farthest:.2f} Km)") # Furthest Distance
            else:
                print("\nRegion not Found")


        # Search Location
        elif choice == 5:
            print("Search Location")
            location_id = input("Enter Location ID to search: ")
            the_location = search_location(locations, location_id)

            if the_location:
                print("\nLocation Found: ")
                view_one_location(the_location)
            else:
                print("\nLocation Not Found!")

        # Default
        else:
            print("Invalid Choice")

        # Display the Menu
        print("""
    The Menu:
        1. View Location Data
        2. Filter Locations by Region
        3. Calculate Distance Between Locations
        4. Generate Region Insights
        5. Search Locations
        6. Exit
        """)
        choice = int(input("Enter Your Choice: "))

    print("Thank you for using the Geographical Data Analysis System")

except ValueError:
    print("\nProgram Terminated. Use Numeric Values Only.")