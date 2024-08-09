# This program records the domain name (instead of the address) where the message was
# sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.
#
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
#
words = list()
domains = dict()

try:
    fhand = open(input('Enter a file name: '))
    #fhand = open('mbox-short.txt')
except:
    print('File does not exist! Try again :)')
    quit()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    email = words[1]
    atpos = email.find('@')
    d = email[atpos + 1:] # extract domain, will be used as key for dictionary
    domains[d] = domains.get(d,0) + 1 # build histogram of domains with counts

print(domains)