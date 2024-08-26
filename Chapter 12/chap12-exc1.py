# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so 
# it can read any web page.

#You can use split('/') to break the URL into its component parts so you can extract the host name 
# for the socket connect call. Add error checking using try and except to handle the condition where 
# the user enters an improperly formatted or non-existent URL.

import socket

url = input('Enter URL: ')

# Determine port number
#if url.startswith('https'):
#    port = 443
#else:
#    port = 80

# Extract hostname
x = url.split('/')
if len(x) > 1:
    domain = x[2]
else:
    domain = x[0]

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((domain, 80))
except:
    print('Invalid URL. Please try again!')
    quit()

cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
    #print(data.decode())

mysock.close()

# Code: https://www.py4e.com/code3/socket1.py

