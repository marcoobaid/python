# Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. 
# You can download the file from www.py4e.com/code3/mbox-short.txt
# 
# Author: Marco Obaid
# marco@obaid.pro
#

fhand = open('mbox-short.txt')

for line in fhand:
    ### Option 1
    #lcontent = line.rstrip()    # Remove end of line character
    #lcontent = lcontent.upper() # Convert line to all UPPERCASE

    ### Option 2
    lcontent = line.rstrip().upper()
    
    print(lcontent)

print('\n### End of file is reached! ###')
