#!/usr/bin/env python3
"""
Network QR Code Generator for Kannada Rajyotsava Website
Windows-compatible version with better encoding handling
"""

import qrcode
import os
import socket
import sys
from pathlib import Path

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        # Connect to a remote address to get local IP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "192.168.1.100"  # Default fallback IP

def create_network_qr_code(url, filename, output_dir):
    """Create a QR code for a network URL"""
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image
        filepath = os.path.join(output_dir, f"{filename}.png")
        img.save(filepath)
        return filepath
    except Exception as e:
        print(f"Error creating QR code for {filename}: {e}")
        return None

def main():
    print("Generating Network QR Codes for Kannada Rajyotsava Flask Website")
    print("=" * 60)
    
    # Configuration - Auto-detect IP or use fallback
    SERVER_IP = get_local_ip()
    SERVER_PORT = "8000"
    BASE_URL = f"http://{SERVER_IP}:{SERVER_PORT}"
    
    print(f"Auto-detected IP address: {SERVER_IP}")
    print(f"Base URL: {BASE_URL}")
    
    # Get script directory and create QR output directory
    script_dir = Path(__file__).parent
    qr_output_dir = script_dir / "qr_network"
    qr_output_dir.mkdir(exist_ok=True)
    
    print(f"QR codes will be saved to: {qr_output_dir}")
    print("These QR codes will work on any device connected to your WiFi network")
    print()
    
    # Regional pages mapping (filename -> display name)
    regional_pages = {
        "north-karnataka": "North Karnataka",
        "central-karnataka": "Central Karnataka", 
        "south-karnataka": "South Karnataka",
        "coastal": "Coastal Karnataka",
        "southeast-karnataka": "South-East Karnataka",
        "northeast-karnataka": "North-East Karnataka"
    }
    
    success_count = 0
    
    # Generate QR codes for each regional page
    for filename, display_name in regional_pages.items():
        url = f"{BASE_URL}/{filename}.html"
        print(f"Creating QR code for {display_name} ({filename}.html)")
        filepath = create_network_qr_code(url, filename, str(qr_output_dir))
        if filepath:
            print(f"Generated: {filepath}")
            success_count += 1
        else:
            print(f"Failed to generate QR code for {filename}")
    
    # Generate QR code for main index page
    index_url = f"{BASE_URL}/"
    print("Creating QR code for Main Page (index.html)")
    index_filepath = create_network_qr_code(index_url, "index", str(qr_output_dir))
    if index_filepath:
        print(f"Generated: {index_filepath}")
        success_count += 1
    
    print()
    print(f"All Network QR codes generated successfully! ({success_count} files)")
    print(f"QR codes saved in: {qr_output_dir}")
    print()
    print("Usage Instructions:")
    print("   1. Start the Flask server: python main.py")
    print(f"   2. Ensure your Flask server is running on {BASE_URL}")
    print("   3. Print these QR codes and display them at your event")
    print("   4. Visitors must be connected to the same WiFi network")
    print("   5. Visitors can scan QR codes to access pages on their mobile devices")
    print()
    print("Alternative ways to start the server:")
    print("   • Using main.py: python main.py")
    print("   • Using run.py: python run.py")
    print("   • Using Flask CLI: set FLASK_APP=app.py && flask run --host=0.0.0.0 --port=8000")
    print()
    print("If your IP address changes:")
    print("   - Re-run this script to generate new QR codes with updated IP")
    print()
    print("Network URLs generated:")
    print(f"   • Main page: {BASE_URL}/")
    for filename, display_name in regional_pages.items():
        print(f"   • {display_name}: {BASE_URL}/{filename}.html")

if __name__ == "__main__":
    main()