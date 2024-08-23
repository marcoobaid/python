# Exercise 1: Write a simple program to simulate the operation of the grep command on
# Unix. Ask the user to enter a regular expression and count the number of lines that
# matched the regular expression:
# 
# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author
# 
# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-
# 
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$
#

import re

count = 0
fhand = open('mbox.txt')

regx = input('Enter a regular expression: ')
#print(regx)

try:
    for line in fhand:
        if re.search(regx , line):
            count = count + 1

    print(f'mbox.txt had {count} lines that matches {regx}')
except:
        print('The expression is invalid. Try again!')


