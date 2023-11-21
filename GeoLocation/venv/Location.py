from urllib.request import urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML
# importing only the necessary for memory saving

api_url = 'https://maps.googleapis.com/maps/api/geocode/xml?'
# the location of Google's geolocation API
#https://maps.googleapis.com/maps/api/geocode/xml?\Playground\?sensor=false&address=Warsaw%2C+Poland&key=AIzaSyADySfAiLC9qj4gwpAY40Fs5B2mBBbwlfE
address = input('Enter location: ')
if len(address) < 1:
    address = "Warsaw, Poland"
    # if no address specified, try my home city :)

key = "AIzaSyCkpAcNqw0RTFARkKxkMPO6nCY80altL-Y"
url = api_url + ENCODE({'sensor': 'false', 'address': address, 'key': key})
#url = "https://maps.googleapis.com/maps/api/geocode/xml?"
#url = api_url + ENCODE({'sensor': 'false', 'address': address})
# putting the parts together in UTF-8 format
print ('\nRetrieving location for:', address)
print(url)

#url = "https://www.google.com/search?q=smoke+shops+in+syracuse&npsic=0&rflfq=1&rlha=0&rllag=43049331,-76143717,1096&tbm=lcl&ved=2ahUKEwikjOGt1_LjAhUEvVkKHbZADu8QtgN6BAgKEAU&tbs=lrf:!2m1!1e2!2m1!1e3!2m1!1e16!3sIAE,lf:1,lf_ui:10&rldoc=1#rlfi=hd:;si:;mv:!1m2!1d43.112463399999996!2d-76.0762149!2m2!1d42.9564054!2d-76.2156646!3m12!1m3!1d75581.61602974584!2d-76.14593975!3d43.0344344!2m3!1f0!2f0!3f0!3m2!1i407!2i622!4f13.1;tbs:lrf:!2m1!1e2!2m1!1e3!2m1!1e16!3sIAE,lf:1,lf_ui:10"
data = OPEN(url).read()
# getting that data
# print ('Retrieved',len(data),'characters')
tree = XML.fromstring(data)
# digging into the XML tree
print(tree)
res = tree.findall('result')

# let's see the results now

lat = res[0].find('geometry').find('location').find('lat').text
# dig into the XML tree to find 'latitude'
lng = res[0].find('geometry').find('location').find('lng').text
# and longitude
lat = float(lat)
lng = float(lng)
if lat < 0:
    lat_c = chr(167)+'S'
else:
    lat_c = chr(167)+'N'
if lng < 0:
    lng_c = chr(167)+'W'
else:
    lng_c = chr(167)+'E'
# format the coordinates to a more appealing form

location = res[0].find('formatted_address').text
location_type = res[0].find('geometry').find('location_type').text
# location holds the geomap unit found by API, based on user input
place_id = res[0].find('place_id').text


# Time for the second part...
url = 'http://maps.googleapis.com/maps/api/place/details/xml?'
# the location of Google Places API
# will need a valid key for that
key = "AIzaSyADySfAiLC9qj4gwpAY40Fs5B2mBBbwlfE"
url = api_url + ENCODE({'placeid': place_id, 'key': key})

data = OPEN(url).read()
tree = XML.fromstring(data)
res = tree.findall('status')[0].text
# rating = res[0].find('rating').text

print("\n==>", location, "<==")
print('Latitude: {0:.3f}{1}'.format(abs(lat), lat_c))
print('Longitude: {0:.3f}{1}'.format(abs(lng), lng_c))
print('Location type:', location_type)
print('Place ID:', place_id)

import createCsv
createCsv.add_location(place_id,location,lat,lng)