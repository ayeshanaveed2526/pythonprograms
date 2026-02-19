# Create a tuple that stores 5 city names.
# Display:
# First city
# Last city
# Ask user to enter a city name
# Use if condition to check:
# If city exists → print "City Found"
# Else → print "City Not Found"
cities = ("Lahore","karachi","Islamabad","Peshawar","Quetta")
print(cities[0])
print(cities[4])
nameofcity = input("Enter your city name:")
if nameofcity in cities:
    print("City Found")
else:
    print("City Not Found")
    