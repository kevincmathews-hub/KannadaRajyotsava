# 🎉 Ethnic Day @ Tismo 2025 - "Festivals of Karnataka"

**Team**: Second Floor Team | **Theme**: Kannada Rajyotsava  
**Event**: Ethnic Day @ Tismo 2025 – "Festivals of Karnataka"

A feature-rich, responsive website celebrating Karnataka's six regions with enhanced interactivity, QR code integration, and bilingual support.

---

## 🎯 **Quick Start**

### **Option 1: Automated Setup (Recommended)**
```bash
# Windows users - Double-click this file
run_setup.bat

# Or run directly
python setup.py
```

### **Option 2: Manual Setup**
```bash
# 1. Generate QR codes
python generate_qr.py

# 2. Start web server
python start_server.py

# 3. Access website at http://localhost:8000
```

---

## 📁 **Project Structure**

```
KannadaRajothsava/
├── 🚀 CORE FILES
│   ├── setup.py                 # Automated setup script
│   ├── start_server.py          # Enhanced web server
│   ├── generate_qr.py           # QR code generator
│   └── run_setup.bat            # Windows batch file
│
├── 🌐 WEB CONTENT
│   └── html/
│       ├── index.html           # Main landing page
│       ├── styles.css           # Enhanced CSS
│       ├── north-karnataka.html # North Karnataka region
│       ├── central-karnataka.html # Central Karnataka region
│       ├── south-karnataka.html # South Karnataka region
│       ├── coastal.html         # Coastal Karnataka region
│       ├── southeast-karnataka.html # South-East Karnataka region
│       └── northeast-karnataka.html # North-East Karnataka region
│
├── 📱 QR CODES
│   └── qr_network/             # Generated QR codes (ready to print)
│       ├── index.png
│       ├── north-karnataka.png
│       └── ... (6 regional QR codes)
│
├── 🖼️ MEDIA ASSETS
│   ├── images/                 # Regional image placeholders
│   │   ├── north-karnataka/
│   │   ├── central-karnataka/
│   │   ├── south-karnataka/
│   │   ├── coastal/
│   │   ├── southeast-karnataka/
│   │   └── northeast-karnataka/
│   └── videos/                 # Regional video placeholders
│       └── ... (same structure as images)
│
└── 📚 DOCUMENTATION
    ├── README.md               # This file
    ├── ENHANCED_README.md      # Detailed feature documentation
    ├── PROJECT_README.md       # Original project documentation
    └── NETWORK_HOSTING_GUIDE.md # Network setup guide
```

---

## 🌟 **Features**

### **✨ Enhanced User Experience**
- **Bilingual Support**: Kannada + English throughout
- **Interactive UI**: Click animations, loading states, hover effects
- **Mobile-First**: Responsive design for all devices
- **Accessibility**: Keyboard navigation, focus indicators
- **Offline Support**: Custom CSS fallbacks

### **🔧 Technical Features**
- **Auto IP Detection**: Automatically detects network IP
- **Security Headers**: Enhanced HTTP security
- **Error Handling**: Comprehensive error recovery
- **QR Integration**: Printable QR codes for mobile access
- **Smart Logging**: Detailed logging for troubleshooting

### **🎨 Design Elements**
- **Karnataka Colors**: Red, Yellow, Gold theme
- **Kannada Typography**: Proper Kannada font support
- **Smooth Animations**: CSS transitions and effects
- **Card-Based Layout**: Modern, clean design

---

## 🏛️ **Karnataka Regions Covered**

1. **🏛️ North Karnataka** (ಉತ್ತರ ಕರ್ನಾಟಕ)
   - Kittur/Bombay Karnataka
   - Districts: Belagavi, Dharwad, Gadag, Bagalkot, Haveri

2. **🌲 Central Karnataka** (ಮಧ್ಯ ಕರ್ನಾಟಕ)
   - Malnad Region
   - Districts: Shivamogga, Chikkamagaluru, Davanagere

3. **👑 South Karnataka** (ದಕ್ಷಿಣ ಕರ್ನಾಟಕ)
   - Mysuru Region
   - Districts: Mysuru, Mandya, Hassan, Chamarajanagara

4. **🏖️ Coastal Karnataka** (ಕರಾವಳಿ ಕರ್ನಾಟಕ)
   - Karavali/Coastal Belt
   - Districts: Udupi, Dakshina Kannada, Uttara Kannada

5. **🌟 South-East Karnataka** (ಆಗ್ನೇಯ ಕರ್ನಾಟಕ)
   - Bengaluru/Old Mysore Expansion
   - Districts: Bengaluru, Ramanagara, Tumakuru, Kolar

6. **🏜️ North-East Karnataka** (ಈಶಾನ್ಯ ಕರ್ನಾಟಕ)
   - Kalyana Karnataka
   - Districts: Kalaburagi, Bidar, Raichur, Yadgir, Bellari

---

## 📱 **QR Code Usage**

### **For Event Organizers:**
1. **Generate**: QR codes auto-created in `qr_network/` folder
2. **Print**: All QR codes ready for printing (PNG format)
3. **Display**: Place printed QR codes at event venue
4. **Instructions**: Include "Connect to WiFi and scan to explore!"

### **For Visitors:**
1. **Connect**: Ensure device is on same WiFi network
2. **Scan**: Any QR code scanner or camera app
3. **Explore**: Navigate through Karnataka regions
4. **Learn**: Discover festivals, culture, and traditions

### **QR Codes Available:**
- **Main Page**: Complete overview of all regions
- **Regional Pages**: Direct access to specific Karnataka regions
- **Mobile Optimized**: Perfect scanning and viewing experience

---

## 🚀 **Deployment Guide**

### **Pre-Event Setup:**
1. **Run Setup**: `python setup.py` or double-click `run_setup.bat`
2. **Verify Server**: Confirm website loads at displayed URL
3. **Print QR Codes**: Print all files from `qr_network/` folder
4. **Test Mobile Access**: Scan QR codes with test device

### **During Event:**
1. **Display QR Codes**: Place at prominent locations
2. **Monitor Server**: Keep terminal/command prompt open
3. **Network Instructions**: Ensure guests connect to WiFi first
4. **Support**: Use server logs for troubleshooting

### **Network Requirements:**
- **Host Computer**: WiFi connected, Python installed, server running
- **Guest Devices**: Same WiFi network, QR scanner app
- **Bandwidth**: Minimal (static content, local hosting)

---

## 🛠️ **Customization**

### **Adding Content:**
- **Images**: Place in respective `images/{region}/` folders
- **Videos**: Place in respective `videos/{region}/` folders
- **Text**: Edit HTML files directly

### **Media Guidelines:**
- **Images**: JPG/PNG, 800x600px or higher, under 2MB
- **Videos**: MP4/WebM, 720p/1080p, under 50MB
- **YouTube**: Update iframe src with video ID

### **Branding:**
- **Colors**: Modify CSS variables in `styles.css`
- **Text**: Update content in HTML files
- **Logos**: Replace placeholder elements

---

## 🔧 **Troubleshooting**

### **Common Issues:**

**QR Codes Don't Work:**
- ✅ Verify server is running
- ✅ Check same WiFi network
- ✅ Test URL manually in browser

**Server Won't Start:**
- ✅ Port 8000 already in use? Try port 8080
- ✅ Check Python installation
- ✅ Verify in correct directory

**Mobile Access Issues:**
- ✅ Confirm WiFi connection (not mobile data)
- ✅ Check Windows Firewall settings
- ✅ Test on host computer first

**IP Address Changed:**
- ✅ Re-run `python generate_qr.py`
- ✅ Print new QR codes
- ✅ Update any hardcoded references

---

## 🎊 **Event Success Tips**

1. **📋 Pre-Event**: Test everything 24 hours before
2. **📍 Placement**: QR codes at eye level, good lighting
3. **📱 Instructions**: Clear "Connect to WiFi first" signs
4. **👥 Support**: Designate tech-savvy team member
5. **📸 Engagement**: Encourage photos and sharing
6. **🎯 Backup**: Have direct URLs available as backup

---

## 🏆 **Credits**

**Created with ❤️ for Tismo's Second Floor Team**

- **Event**: Ethnic Day @ Tismo 2025 – "Festivals of Karnataka"
- **Team**: Second Floor Team
- **Theme**: Kannada Rajyotsava
- **Focus**: Celebrating Karnataka's diversity and festivals

**Technical Features:**
- Enhanced security and performance
- Bilingual Kannada-English support
- Mobile-first responsive design
- QR code integration
- Interactive user experience

---

## 🎉 **Ready to Celebrate!**

Your **Ethnic Day @ Tismo 2025** website is ready with:

✅ **Complete Tismo Branding**  
✅ **Second Floor Team Recognition**  
✅ **Kannada Rajyotsava Theme**  
✅ **6 Karnataka Regional Pages**  
✅ **Mobile-Optimized QR Codes**  
✅ **Interactive Features**  
✅ **Offline Capabilities**  

**ತಿಸ್ಮೋದ ಎರಡನೇ ಮಹಡಿ ತಂಡದ ಪರವಾಗಿ ಕರ್ನಾಟಕದ ಕೀರ್ತಿ ಸದಾ ಬೆಳೆಯಲಿ!**

**Happy Ethnic Day @ Tismo 2025! 🎊**