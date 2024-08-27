# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, 
# (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. 
# Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document 
# contents.

import urllib.request, urllib.parse, urllib.error

url = input('Enter URL: ')

# Extract hostname
x = url.split('/')
if len(x) > 1:
    domain = x[2]
else:
    domain = x[0]

if '.' not in domain:
    print('\nInvalid URL. Please try again!\n')
    quit()

# Establish a socket connection
try:
    fhand = urllib.request.urlopen(url)
except:
    print('\nInvalid URL. Please try again!\n')
    quit()

total_characters = 0
display_limit = 3000

for line in fhand:
    line = line.decode().strip()
    line_characters = len(line)
    total_characters += line_characters
    # Display up to 3000 characters
    if total_characters <= display_limit:
        print(line)
    elif total_characters - line_characters < display_limit:
        print(line[:display_limit - (total_characters - line_characters)])
        break
