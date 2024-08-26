import socket

def fetch_webpage(url):
    # Parse the URL to extract the host and path
    host = url.split('/')[2]
    path = '/' + '/'.join(url.split('/')[3:])

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((host, 80))

    # Send an HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    s.send(request.encode())

    # Receive the response
    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data

    # Close the socket
    s.close()

    # Decode and print the response
    print(response.decode())

# Example usage:
#fetch_webpage("https://www.py4e.com/code3/intro.txt")
fetch_webpage("https://www.py4e.com/lectures3/Pythonlearn-11-Regex-Handout.txt")

# Explanation:
# 1. Parse the URL: Extract the host and path from the URL.
# 2. Create a Socket: Create a socket object using socket.AF_INET and socket.SOCK_STREAM.
# 3. Connect to the Server: Connect to the server on port 80 (HTTP).
# 4. Send an HTTP GET Request: Send a properly formatted HTTP GET request to the server.
# 5. Receive the Response: Continuously receive data from the server until there’s no more data.
# 6. Close the Socket: Close the socket connection.
# 7.Print the Response: Decode and print the response.
#
# This script will fetch and print the HTML content of the specified webpage. 
# Note that this example uses HTTP and may not work with HTTPS URLs.
#

