from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myGeoCodeApp")
location = geolocator.geocode("Acharya Nagarjuna University")
print(location.address)

print((location.latitude, location.longitude))
