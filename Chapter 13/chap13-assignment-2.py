# In this assignment you will write a Python program somewhat similar to 
# http://www.py4e.com/code3/json2.py. 
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse 
# and extract the comment counts from the JSON data, compute the sum of the numbers in the file 
# and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# 
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_2037192.json (Sum ends with 53)
#
import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1 : 
    #url = 'http://py4e-data.dr-chuck.net/comments_42.json'
    url = 'http://py4e-data.dr-chuck.net/comments_2037192.json '

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

# load json data
info = json.loads(data)
# generate comments list
lst = info['comments']
nums = list()

# generate list of values for "count" key as integers
for item in lst:
    nums.append(int(item['count']))

# Calculate number of values and their total
print('Count:', len(nums))
print('Sum:', sum(nums))

