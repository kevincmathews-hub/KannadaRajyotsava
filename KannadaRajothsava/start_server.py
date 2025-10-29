#!/usr/bin/env python3
"""
Simple HTTP Server for Kannada Rajyotsava Webs            print("🎯 Available pages:")
            print(f"   • Main page: http://{local_ip}:{PORT}/")
            print(f"   • North Karnataka: http://{local_ip}:{PORT}/north-karnataka.html")
            print(f"   • Central Karnataka: http://{local_ip}:{PORT}/central-karnataka.html")
            print(f"   • South Karnataka: http://{local_ip}:{PORT}/south-karnataka.html")
            print(f"   • Coastal Karnataka: http://{local_ip}:{PORT}/coastal.html")
            print(f"   • South-East Karnataka: http://{local_ip}:{PORT}/southeast-karnataka.html")
            print(f"   • North-East Karnataka: http://{local_ip}:{PORT}/northeast-karnataka.html")ves the website on local network for QR code access
"""

import http.server
import socketserver
import os
import sys
import socket
import logging
from pathlib import Path
from datetime import datetime

class EnhancedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Enhanced HTTP handler with security headers and logging"""
    
    def end_headers(self):
        # Add security headers
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('X-XSS-Protection', '1; mode=block')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Enhanced logging with timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] {format % args}")

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        # Connect to a remote address to get local IP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "localhost"

def start_server():
    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Change to the directory containing the HTML files
    script_dir = Path(__file__).parent
    html_dir = script_dir / "html"
    
    if not html_dir.exists():
        print("❌ Error: html directory not found!")
        print(f"Looking for: {html_dir}")
        return
    
    # Change to html directory so it serves as the root
    os.chdir(html_dir)
    
    # Server configuration
    PORT = 8000
    HOST = "0.0.0.0"  # Listen on all network interfaces
    
    # Get local IP address
    local_ip = get_local_ip()
    
    # Create server with enhanced handler
    Handler = EnhancedHTTPRequestHandler
    
    try:
        with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
            print("🌐 Kannada Rajyotsava Website Server Starting...")
            print("📡 Server running on all network interfaces")
            print(f"🔗 Local access: http://localhost:{PORT}")
            print(f"🔗 Network access: http://{local_ip}:{PORT}")
            print(f"📱 Mobile devices on same network can access via: http://{local_ip}:{PORT}")
            print(f"📁 Serving files from: {html_dir}")
            print("\n🎯 Available pages:")
            print(f"   • Main page: http://192.168.2.212:{PORT}/")
            print(f"   • North Karnataka: http://192.168.2.212:{PORT}/north-karnataka.html")
            print(f"   • Central Karnataka: http://192.168.2.212:{PORT}/central-karnataka.html")
            print(f"   • South Karnataka: http://192.168.2.212:{PORT}/south-karnataka.html")
            print(f"   • Coastal Karnataka: http://192.168.2.212:{PORT}/coastal.html")
            print(f"   • South-East Karnataka: http://192.168.2.212:{PORT}/southeast-karnataka.html")
            print(f"   • North-East Karnataka: http://192.168.2.212:{PORT}/northeast-karnataka.html")
            print("\n💡 Instructions:")
            print("   1. Make sure all devices are on the same WiFi network")
            print("   2. Generate QR codes using: python generate_qr_network.py")
            print("   3. Print and display QR codes at your event")
            print("   4. Visitors can scan QR codes to access pages")
            print("\n🛑 Press Ctrl+C to stop the server")
            print("=" * 70)
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Error: Port {PORT} is already in use!")
            print("   Try closing other applications using this port, or")
            print("   Change the PORT variable in this script to a different number (e.g., 8080)")
        else:
            print(f"❌ Error starting server: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    start_server()