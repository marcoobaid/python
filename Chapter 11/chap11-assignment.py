# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.
#
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your 
# testing and the other is the actual data you need to process for the assignment.
# 
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt 
# (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_2037187.txt 
# (There are 85 values and the sum ends with 668)
# 
import re

length = 0
total = 0

#fhand = open('regex_sum_42.txt')
fhand = open('regex_sum_2037187.txt')

for line in fhand:
    x = re.findall(r'[0-9]+', line)
    length = len(x)
    if length < 1:
        continue
    else:
        i = 0
        while i < length :
            total += int(x[i])
            i += 1

print(total)
