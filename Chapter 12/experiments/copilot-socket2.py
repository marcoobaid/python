import socket
import ssl

def fetch_https_webpage(url):
    # Parse the URL to extract the host and path
    host = url.split('/')[2]
    path = '/' + '/'.join(url.split('/')[3:])

    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with SSL
    context = ssl.create_default_context()
    ssock = context.wrap_socket(sock, server_hostname=host)

    # Connect to the server
    ssock.connect((host, 443))

    # Send an HTTPS GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    ssock.send(request.encode())

    # Receive the response
    response = b""
    while True:
        data = ssock.recv(4096)
        if not data:
            break
        response += data

    # Close the socket
    ssock.close()

    # Decode and print the response
    print(response.decode())

# Example usage:
fetch_https_webpage("https://raw.githubusercontent.com/csev/py4e/master/book3/00-cover.old")
