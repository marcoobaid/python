# Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved
# HTML document and display the count of the paragraphs as the output of your program. 
# Do not display the paragraph text, only count them. 
# Test your program on several small web pages as well as some larger web pages.
# Code: https://www.py4e.com/code3/urllinks.py
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
except:
    print('\nInvalid URL. Please try again!\n')
    quit()

# Find paragraph tags
paragraphs = soup.find_all('p')
# Count extracted tags
count = 0
for p in paragraphs:
    count +=1

print(f'{count} paragraph tags found on this page.')


