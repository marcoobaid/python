# Scraping Numbers from HTML using BeautifulSoup 
# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
# The program will use urllib to read the HTML from the data files below, and parse the data, 
# extracting numbers and compute the sum of the numbers in the file.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_2037189.html (Sum ends with 19)
#
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
total = 0
for tag in tags:
    #print(tag)
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print(tag.contents[0])
    #print('Attrs:', tag.attrs)
    count +=1
    total += int(tag.contents[0])

print(f'Count {count}')
print(f'Sum {total}')