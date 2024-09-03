# The program will use urllib to read the HTML from the data files below, extract the href= vaues from
# the anchor tags, scan for a tag that is in a particular position relative to the first name in 
# the list, follow that link and repeat the process a number of times and report the last name you find.
# 
# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). 
# Follow that link. Repeat this process 4 times. 
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
#
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Darrie.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
# The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: L
#
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
except:
    print('Invalid URL. Please try again!')
    quit()

try:
     count = int(input('Enter count: '))
     position = int(input('Enter position: '))
except:
     print("Count and Position must be a digit. Please try again!")
     quit() 

    
print(f'Retrieving: {url}')

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    i = 1
    for tag in tags:
        if i == position:
            url = tag.get('href', None)
            print(f'Retrieving: {url}')
            break
        i += 1
    count -= 1
