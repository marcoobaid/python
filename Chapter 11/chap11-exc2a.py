# Exercise 2: Write a program to look for lines of the form:
# 
# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the 
# findall() method. Compute the average of the numbers and print out the average 
# as an integer.
# 
# Enter file:mbox.txt
# 38549
# 
# Enter file:mbox-short.txt
# 39756
#

import re

count = 0
total = 0
avrg = 0

fhand = open(input('Enter file: '))

for line in fhand:
    line = line.rstrip()
    x = re.findall(r'New\sRevision: ([0-9]{5})', line)
    if len(x) != 1: continue 
    number = int(x[0])
    count = count + 1
    total = total + number

avrg = int(total/count)
print(avrg)
