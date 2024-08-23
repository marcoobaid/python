import re
#s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
#lst = re.findall(r'\S+@\S+', s)
#print(lst)
#
## Code: https://www.py4e.com/code3/re05.py

# Search for lines that have an at sign between characters
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #x = re.findall('\S+@\S+', line)
    #x = re.findall(r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    #x = re.findall(r'^X\S*: ([0-9.]+)', line)
    #x = re.findall(r'^Details:.*rev=([0-9]+)', line)
    x = re.findall(r'^From .* ([0-9][0-9]):', line)
    if len(x) > 0:
        print(x)

# Code: https://www.py4e.com/code3/re06.py

