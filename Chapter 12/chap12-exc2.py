# Exercise 2: Change your socket program so that it counts the number of characters it has received 
# and stops displaying any text after it has shown 3000 characters. The program should retrieve 
# the entire document and count the total number of characters and display the count of the number of 
# characters at the end of the document.

import socket

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
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((domain, 80))
except:
    print('\nInvalid URL. Please try again!\n')
    quit()

# Send a GET request
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# Receive data in chunks
response = b""
total_characters = 0
display_limit = 3000
while True:
    data = mysock.recv(4096)
    if not data:
        break
    response += data
    total_characters += len(data)
    #print(data.decode())

    # Display up to 3000 characters
    if total_characters <= display_limit:
        print(data.decode(), end='')
    elif total_characters - len(data) < display_limit:
        print(data[:display_limit - (total_characters - len(data))].decode(), end='')

mysock.close()

# Print the total number of characters received
print('\n\n******************************************')
print(f"Total number of characters received: {total_characters}")
print('******************************************\n')

# Offer to read the entire fetched response
followup = input('Read the entire file? (Y/n): ')
if followup in ['Y', 'y', '']:
    print(response.decode())
else:
    print('\nThank you!\n') 

# Code: https://www.py4e.com/code3/socket1.py
