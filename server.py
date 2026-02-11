#!/usr/bin/env python3
"""
Local HTTP Server for GesundheitProfi
Serves files on local network at http://<IP>:8000
"""

import http.server
import socketserver
import os
import socket

PORT = 8000

# Get local IP address
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# Change to the directory with the website
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

print("=" * 60)
print("🌐 GesundheitProfi - Local Server")
print("=" * 60)
print(f"\n📍 Serving at:")
print(f"   Local:  http://localhost:{PORT}")
print(f"   Network: http://{get_local_ip()}:{PORT}")
print(f"\n📁 Directory: {os.getcwd()}")
print("\n🛑 Press Ctrl+C to stop\n")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
