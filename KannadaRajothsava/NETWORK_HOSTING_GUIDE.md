# 🌐 Ethnic Day @ Tismo 2025 - Network Hosting Guide

## 📋 Overview
This guide helps you host the **"Festivals of Karnataka"** website for **Tismo's Second Floor Team** on your local network so that visitors can access it by scanning QR codes on their mobile devices during **Ethnic Day @ Tismo 2025**.

## 🚀 Quick Start

### Step 1: Start the Server
```bash
python start_server.py
```

### Step 2: Access the Website
- **Local access**: http://localhost:8000
- **Network access**: http://192.168.2.212:8000
- **Mobile access**: Scan QR codes from `qr_network/` folder

## 📱 QR Code Setup

### Network QR Codes Location
All network QR codes are saved in: `qr_network/`

### Available QR Codes:
- `index.png` - Main landing page
- `north-karnataka.png` - North Karnataka region
- `central-karnataka.png` - Central Karnataka region  
- `south-karnataka.png` - South Karnataka region
- `coastal.png` - Coastal Karnataka region
- `southeast-karnataka.png` - South-East Karnataka region
- `northeast-karnataka.png` - North-East Karnataka region

### Print Instructions:
1. Print all QR codes from the `qr_network/` folder
2. Display them at your event venue
3. Add labels like "North Karnataka", "Central Karnataka", etc.
4. Include instructions: "Connect to WiFi and scan to explore!"

## 🔧 Server Management

### Start Server:
```bash
python start_server.py
```

### Stop Server:
Press `Ctrl+C` in the terminal where the server is running

### Check Server Status:
If the server is running, you should see:
```
🌐 Kannada Rajyotsava Website Server Starting...
📡 Server running on all network interfaces
🔗 Network access: http://192.168.2.212:8000
```

## 📋 Network Requirements

### For the Host Computer:
- Must be connected to WiFi network
- Python must be installed with required packages
- Server must be running (`python start_server.py`)
- Windows Firewall may need to allow Python/HTTP access

### For Visitor Devices:
- Must be connected to the **same WiFi network**
- Any smartphone with QR scanner (most camera apps work)
- Any web browser (Chrome, Safari, Firefox, etc.)

## 🔍 Troubleshooting

### Problem: QR codes don't work
**Solutions:**
1. Verify server is running: `python start_server.py`
2. Check that devices are on same WiFi network
3. Test URL manually: http://192.168.2.212:8000
4. Check Windows Firewall settings

### Problem: "Address already in use"
**Solutions:**
1. Close other applications using port 8000
2. Or edit `start_server.py` and change `PORT = 8000` to `PORT = 8080`
3. Regenerate QR codes with new port: `python generate_qr_network.py`

### Problem: IP address changed
**Solutions:**
1. Find new IP: `ipconfig | findstr "IPv4"`
2. Update `SERVER_IP` in `generate_qr_network.py`
3. Update `SERVER_IP` in `start_server.py`  
4. Regenerate QR codes: `python generate_qr_network.py`

### Problem: Mobile devices can't access
**Solutions:**
1. Ensure all devices are on same WiFi (not mobile data)
2. Test the URL in mobile browser first
3. Check Windows Firewall - allow Python through firewall
4. Try accessing from computer browser first: http://192.168.2.212:8000

## 🌐 URLs Generated

When server is running, these URLs will be accessible:

| Page | URL |
|------|-----|
| Main Page | http://192.168.2.212:8000/ |
| North Karnataka | http://192.168.2.212:8000/north-karnataka.html |
| Central Karnataka | http://192.168.2.212:8000/central-karnataka.html |
| South Karnataka | http://192.168.2.212:8000/south-karnataka.html |
| Coastal Karnataka | http://192.168.2.212:8000/coastal.html |
| South-East Karnataka | http://192.168.2.212:8000/southeast-karnataka.html |
| North-East Karnataka | http://192.168.2.212:8000/northeast-karnataka.html |

## 📁 File Structure

```
KannadaRajothsava/
├── start_server.py              # HTTP server script
├── generate_qr_network.py       # Network QR generator
├── html/                        # Website files (served by server)
│   ├── index.html
│   ├── north-karnataka.html
│   ├── central-karnataka.html
│   ├── south-karnataka.html
│   ├── coastal.html
│   ├── southeast-karnataka.html
│   └── northeast-karnataka.html
├── qr_network/                  # Network QR codes (print these!)
│   ├── index.png
│   ├── north-karnataka.png
│   ├── central-karnataka.png
│   ├── south-karnataka.png
│   ├── coastal.png
│   ├── southeast-karnataka.png
│   └── northeast-karnataka.png
└── qr/                          # Local QR codes (for reference only)
```

## 🎯 Event Setup Checklist

- [ ] Server is running: `python start_server.py`
- [ ] QR codes are printed from `qr_network/` folder
- [ ] QR codes are labeled and displayed at venue
- [ ] Test with your own mobile device first
- [ ] WiFi network name and password available for guests
- [ ] Instructions posted: "Connect to WiFi, then scan QR codes"
- [ ] Computer hosting server remains connected and powered on

## 💡 Tips for Success

1. **Test Before Event**: Always test QR codes with mobile devices before your event
2. **WiFi Instructions**: Clearly post WiFi network name and password
3. **Multiple Networks**: If you have multiple WiFi networks, ensure everyone uses the same one
4. **Server Stability**: Keep the host computer powered on and connected throughout the event
5. **Backup Plan**: Keep local file access available in case of network issues

## 🔒 Security Notes

- Server only runs on local network (not internet accessible)
- Only people on your WiFi network can access the website
- Server serves static files only (HTML, CSS, images)
- No sensitive data or user input handling
- Stop server when event is complete

---

**Happy Kannada Rajyotsava Celebration! 🎉**