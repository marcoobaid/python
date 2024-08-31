# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and 
# a blank line have been received. 
# * Remember that recv receives characters (newlines and all), not lines. *
#
import socket

def receive_data_after_header(s):
    """Receives data from a socket after the HTTP header."""

    header_ended = False
    data = b""

    while True:
        chunk = s.recv(512)
        if not chunk:
            break

        if not header_ended:
            # Check for the end of the header (empty line)
            if b"\r\n\r\n" in chunk:
                header_ended = True
                data += chunk.split(b"\r\n\r\n", 1)[1]  # Extract data after header
        else:
            data += chunk

    return data

url = input('Enter URL: ')

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

# Send an HTTP request
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)
#request = "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
mysock.sendall(cmd)

# Receive the response and extract data after the header
data = receive_data_after_header(mysock)

# Close the socket
mysock.close()

# Print the received data
print(f'\n{data.decode()}')
