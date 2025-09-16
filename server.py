#!/usr/bin/env python3
"""
Simple static file server for OvinoSul website
Serves HTML, CSS, JS, and other static assets with proper cache headers
"""

import http.server
import socketserver
import os
import mimetypes
from urllib.parse import urlparse

class StaticFileHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add cache control headers to prevent aggressive caching during development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        # Handle root path
        if self.path == '/':
            self.path = '/index.html'
        
        # Serve the requested file
        super().do_GET()

def run_server():
    PORT = 5000
    HOST = '0.0.0.0'
    
    print(f"Starting OvinoSul server on {HOST}:{PORT}")
    print("Serving static files with cache disabled for development")
    print("Visit: http://localhost:5000 or your Replit preview URL")
    
    with socketserver.TCPServer((HOST, PORT), StaticFileHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.shutdown()

if __name__ == "__main__":
    run_server()