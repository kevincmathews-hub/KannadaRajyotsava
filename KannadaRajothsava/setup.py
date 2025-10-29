#!/usr/bin/env python3
"""
Automated Setup Script for Kannada Rajyotsava Website
Handles dependency installation, IP detection, QR code generation, and server startup
"""

import subprocess
import sys
import os
import socket
import time
from pathlib import Path

def print_header():
    """Print welcome header"""
    print("=" * 70)
    print("🎉 KANNADA RAJYOTSAVA 2025 - AUTOMATED SETUP 🎉")
    print("=" * 70)
    print("ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ - ಸ್ವಯಂಚಾಲಿತ ಸೆಟಪ್")
    print("Automated Setup for Office Cultural Celebration")
    print("=" * 70)

def check_python_version():
    """Check if Python version is compatible"""
    print("\n🔍 Checking Python version...")
    if sys.version_info < (3, 6):
        print("❌ Error: Python 3.6 or higher is required!")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]} - Compatible!")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("\n📦 Installing dependencies...")
    
    # Check if requirements.txt exists
    requirements_file = Path(__file__).parent / 'requirements.txt'
    if requirements_file.exists():
        try:
            print("   Installing from requirements.txt...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                         check=True, capture_output=True, text=True)
            print("   ✅ All dependencies from requirements.txt installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Failed to install from requirements.txt: {e}")
            # Fallback to manual installation
    
    # Fallback: Install individual packages
    required_packages = ['Flask>=3.1.0', 'qrcode[pil]>=7.4.0', 'Pillow>=10.0.0']
    
    for package in required_packages:
        try:
            print(f"   Installing {package}...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', package], 
                         check=True, capture_output=True, text=True)
            print(f"   ✅ {package} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Failed to install {package}: {e}")
            return False
    
    print("✅ All dependencies installed successfully!")
    return True

def get_local_ip():
    """Get the local IP address"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "192.168.1.100"

def check_directory_structure():
    """Verify project directory structure"""
    print("\n📁 Checking directory structure...")
    
    required_dirs = ['html', 'images', 'videos', 'qr_network']
    required_files = ['main.py', 'app.py', 'config.py', 'generate_qr.py']
    
    script_dir = Path(__file__).parent
    
    # Check directories
    for dir_name in required_dirs:
        dir_path = script_dir / dir_name
        if not dir_path.exists():
            print(f"   📁 Creating missing directory: {dir_name}")
            dir_path.mkdir(exist_ok=True)
        print(f"   ✅ Directory found: {dir_name}")
    
    # Check files
    for file_name in required_files:
        file_path = script_dir / file_name
        if not file_path.exists():
            print(f"   ❌ Missing required file: {file_name}")
            return False
        print(f"   ✅ File found: {file_name}")
    
    return True

def generate_qr_codes():
    """Generate QR codes for the website"""
    print("\n🔳 Generating QR codes...")
    try:
        subprocess.run([sys.executable, 'generate_qr.py'], 
                      capture_output=True, text=True, check=True)
        print("✅ QR codes generated successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to generate QR codes: {e}")
        print("Output:", e.stdout)
        print("Error:", e.stderr)
        return False

def start_flask_server_background():
    """Start the Flask server in background"""
    print("\n🌐 Starting Flask web server...")
    local_ip = get_local_ip()
    
    try:
        # Start Flask server in background
        process = subprocess.Popen([sys.executable, 'main.py'], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE)
        
        # Give server time to start
        time.sleep(3)
        
        # Check if server is running
        if process.poll() is None:
            print("✅ Flask server started successfully!")
            print("🔗 Local access: http://localhost:8000")
            print(f"🔗 Network access: http://{local_ip}:8000")
            print("📱 Mobile access: Scan QR codes from qr_network/ folder")
            return process
        else:
            print("❌ Flask server failed to start")
            return None
            
    except Exception as e:
        print(f"❌ Error starting Flask server: {e}")
        return None

def print_usage_instructions():
    """Print final usage instructions"""
    local_ip = get_local_ip()
    
    print("\n" + "=" * 70)
    print("🎯 SETUP COMPLETE - USAGE INSTRUCTIONS")
    print("=" * 70)
    
    print("\n📱 For Mobile Users:")
    print("   1. Connect your mobile device to the same WiFi network")
    print("   2. Print QR codes from the 'qr_network' folder")
    print("   3. Scan any QR code to access the website")
    
    print("\n💻 For Desktop Users:")
    print("   • Local access: http://localhost:8000")
    print(f"   • Network access: http://{local_ip}:8000")
    
    print("\n📂 QR Codes Location:")
    print("   • All QR codes are in: qr_network/")
    print("   • Print these files for your event")
    
    print("\n🔧 Troubleshooting:")
    print("   • If IP changes, re-run this setup script")
    print("   • Check Windows Firewall if mobile access fails")
    print("   • Ensure all devices are on same WiFi network")
    
    print("\n🎉 Ready for Kannada Rajyotsava Celebration!")
    print("   ಕರ್ನಾಟಕದ ಕೀರ್ತಿ ಸದಾ ಬೆಳೆಯಲಿ! | May Karnataka's glory always grow!")

def main():
    """Main setup function"""
    print_header()
    
    # Step 1: Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Step 2: Check directory structure
    if not check_directory_structure():
        print("\n❌ Directory structure check failed!")
        sys.exit(1)
    
    # Step 3: Install dependencies
    if not install_dependencies():
        print("\n❌ Dependency installation failed!")
        sys.exit(1)
    
    # Step 4: Generate QR codes
    if not generate_qr_codes():
        print("\n❌ QR code generation failed!")
        sys.exit(1)
    
    # Step 5: Start Flask server
    server_process = start_flask_server_background()
    if not server_process:
        print("\n❌ Flask server startup failed!")
        sys.exit(1)
    
    # Step 6: Print instructions
    print_usage_instructions()
    
    # Keep script running to maintain server
    try:
        print("\n🛑 Press Ctrl+C to stop the server and exit...")
        server_process.wait()
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down server...")
        server_process.terminate()
        server_process.wait()
        print("✅ Server stopped. Thank you for celebrating with us!")
        print("   ಧನ್ಯವಾದಗಳು! | Thank you!")

if __name__ == "__main__":
    main()