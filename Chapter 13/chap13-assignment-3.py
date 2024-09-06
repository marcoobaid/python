# In this assignment you will write a Python program somewhat similar to 
# http://www.py4e.com/code3/opengeo.py. 
# The program will prompt for a location, contact a web service and retrieve JSON for the web service 
# and parse that data, and retrieve the first plus_code from the JSON. An Open Location Code is a textual 
# identifier that is another form of address based on the location of the address.
#
import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters') #, data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    # Extract textual identifier
    plus_code = js['features'][0]['properties']['plus_code']
    print(plus_code)


