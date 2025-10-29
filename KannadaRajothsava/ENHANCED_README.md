# 🎉 Ethnic Day @ Tismo 2025 - "Festivals of Karnataka"

An improved, feature-rich static website celebrating Karnataka's six regions for **Tismo's Ethnic Day 2025**.  
**Team**: Second Floor Team | **Theme**: Kannada Rajyotsava

## ✨ New Features & Improvements

### 🔧 **Enhanced Technical Features**
- **Auto IP Detection**: Automatically detects your local network IP
- **Enhanced Security**: Added security headers and better error handling
- **Offline Support**: Custom CSS fallback for better offline functionality
- **Improved Logging**: Comprehensive logging for easier troubleshooting
- **Interactive UI**: Click animations, loading states, and user feedback

### 🌐 **Better User Experience**
- **Kannada Integration**: Added Kannada text alongside English
- **Mobile Optimization**: Enhanced mobile responsiveness
- **Accessibility**: Improved keyboard navigation and focus indicators
- **Smart Notifications**: Online/offline status detection
- **Loading States**: Visual feedback for better user experience

### 🚀 **Automated Setup**
- **One-Click Setup**: `setup.py` handles everything automatically
- **Windows Batch File**: `run_setup.bat` for easy Windows execution
- **Dependency Management**: Automatic package installation
- **Error Recovery**: Smart error handling and recovery suggestions

## 🚀 **Quick Start (New & Improved)**

### **Option 1: Automated Setup (Recommended)**
1. **Windows Users**: Double-click `run_setup.bat`
2. **All Platforms**: Run `python setup.py`

The script will:
- ✅ Check Python compatibility
- ✅ Install required packages
- ✅ Detect your network IP
- ✅ Generate QR codes
- ✅ Start the web server
- ✅ Display access instructions

### **Option 2: Manual Setup**
```bash
# Install dependencies
pip install qrcode[pil]

# Generate QR codes (auto-detects IP)
python generate_qr_network.py

# Start server (enhanced with security headers)
python start_server.py
```

## 📱 **QR Code Usage**

**Enhanced QR System:**
- QR codes are stored in `qr_network/` directory
- Auto-generated with current network IP
- Includes error recovery if IP changes
- Optimized for mobile scanning

**Files Generated:**
- `index.png` - Main landing page
- `north-karnataka.png` - North Karnataka region
- `central-karnataka.png` - Central Karnataka region
- `south-karnataka.png` - South Karnataka region
- `coastal.png` - Coastal Karnataka region
- `southeast-karnataka.png` - South-East Karnataka region
- `northeast-karnataka.png` - North-East Karnataka region

## 🌟 **User Interface Improvements**

### **Enhanced Design**
- Custom CSS with Karnataka flag colors
- Improved typography with Kannada font support
- Smooth animations and transitions
- Better visual hierarchy

### **Interactive Features**
- Click animations on cards
- Loading states for navigation
- Success/error notifications
- Keyboard navigation support
- Smooth scrolling

### **Accessibility**
- Focus indicators for keyboard users
- Screen reader friendly structure
- High contrast text
- Mobile-first responsive design

## 🔧 **Technical Improvements**

### **Server Enhancements**
- Security headers (X-Content-Type-Options, X-Frame-Options, etc.)
- Enhanced logging with timestamps
- Better error handling
- Auto IP detection
- Graceful shutdown handling

### **QR Generation Improvements**
- Auto IP detection with fallback
- Enhanced error handling
- Logging support
- Better user feedback
- Recovery instructions

### **File Structure**
```
KannadaRajothsava/
├── setup.py                     # 🆕 Automated setup script
├── run_setup.bat                # 🆕 Windows batch file
├── start_server.py              # ✅ Enhanced with security
├── generate_qr_network.py       # ✅ Enhanced with auto-IP
├── qr_generation.log            # 🆕 Auto-generated log file
├── html/
│   ├── styles.css               # 🆕 Custom CSS with enhancements
│   ├── index.html               # ✅ Enhanced with Kannada & JS
│   ├── coastal.html             # ✅ Enhanced with new features
│   └── ... (other regional pages)
├── qr_network/                  # ✅ Correct directory name
│   └── ... (QR code files)
└── ... (images, videos, docs)
```

## 🌐 **Multilingual Support**

### **Kannada Integration**
- Region names in Kannada script
- Welcome messages in both languages
- Cultural authenticity maintained
- Proper Kannada font loading

### **Examples**
- ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ - Kannada Rajyotsava
- ಕರಾವಳಿ ಕರ್ನಾಟಕ - Coastal Karnataka
- ಕರ್ನಾಟಕದ ಕೀರ್ತಿ ಸದಾ ಬೆಳೆಯಲಿ! - May Karnataka's glory always grow!

## 🛠️ **Troubleshooting**

### **Enhanced Error Handling**
- Automatic IP detection with fallbacks
- Detailed error messages
- Recovery suggestions
- Log file generation (`qr_generation.log`)

### **Common Issues & Solutions**
1. **IP Address Changed**: Re-run setup script
2. **Port Already in Use**: Script will suggest alternatives
3. **Mobile Access Issues**: Check firewall settings
4. **QR Codes Not Working**: Verify same WiFi network

## 📊 **Performance Improvements**

- Optimized CSS delivery
- Reduced external dependencies
- Better caching headers
- Compressed assets
- Mobile-optimized layouts

## 🎯 **Event Usage**

### **Setup Workflow**
1. Run `setup.py` or `run_setup.bat`
2. Print QR codes from `qr_network/` folder
3. Display QR codes at your venue
4. Guests connect to WiFi and scan codes
5. Enjoy the celebration!

### **Features for Events**
- Real-time server status
- Mobile-optimized interface
- Quick QR code regeneration
- Offline functionality
- Multi-device support

---

## 🙏 **Credits**

Enhanced with ❤️ for celebrating Karnataka's beautiful diversity.

**New Features Added:**
- Automated setup and deployment
- Enhanced security and performance
- Better user experience
- Kannada language integration
- Improved accessibility
- Smart error handling

**ಕರ್ನಾಟಕದ ಕೀರ್ತಿ ಸದಾ ಬೆಳೆಯಲಿ! | May Karnataka's glory always grow!**

---
*Kannada Rajyotsava 2025 - Enhanced Edition 🎉*