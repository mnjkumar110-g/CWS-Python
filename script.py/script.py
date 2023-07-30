import socket
import os
import pyqrcode
import png
import webbrowser
from pyqrcode import QRCode
from http.server import CGIHTTPRequestHandler, HTTPServer
import time
from time import sleep


hostname= socket.gethostname() # PC Name
print(hostname)

ip=socket.gethostbyname(hostname) # Get IP Address
serverPort = 8080
print(ip)

cirrent_dir=os.getcwd()
print(cirrent_dir)

webServer=HTTPServer((hostname,serverPort),CGIHTTPRequestHandler)
print("Server started http://%s:%s" % (ip, serverPort))

try:
    url=pyqrcode.create(f"http://{ip}:{serverPort}")
    url.png("myqr.png", scale=6)
    sleep(3)
    webbrowser.open("myqr.png")
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Server stopped.")