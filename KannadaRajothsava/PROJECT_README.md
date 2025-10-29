# Ethnic Day @ Tismo 2025 - "Festivals of Karnataka"

A festive static website celebrating the six regions of Karnataka for Tismo's Ethnic Day 2025. 
Proudly presented by the **Second Floor Team** with the theme **"Kannada Rajyotsava"**.

## 🎉 Project Overview

**Tismo's Second Floor Team** presents this beautiful, responsive website for **Ethnic Day @ Tismo 2025** with the theme **"Festivals of Karnataka"**, showcasing six distinct regions of Karnataka:
- **North Karnataka** (ಉತ್ತರ ಕರ್ನಾಟಕ) - Kittur/Bombay Karnataka: Belagavi, Dharwad, Gadag, Bagalkot, Haveri
- **Central Karnataka** (ಮಧ್ಯ ಕರ್ನಾಟಕ) - Malnad Region: Shivamogga, Chikkamagaluru, Davanagere
- **South Karnataka** (ದಕ್ಷಿಣ ಕರ್ನಾಟಕ) - Mysuru Region: Mysuru, Mandya, Hassan, Chamarajanagara
- **Coastal Karnataka** (ಕರಾವಳಿ ಕರ್ನಾಟಕ) - Karavali/Coastal Belt: Udupi, Dakshina Kannada, Uttara Kannada
- **South-East Karnataka** (ಆಗ್ನೇಯ ಕರ್ನಾಟಕ) - Bengaluru/Old Mysore Expansion: Bengaluru, Ramanagara, Tumakuru, Kolar
- **North-East Karnataka** (ಈಶಾನ್ಯ ಕರ್ನಾಟಕ) - Kalyana Karnataka: Kalaburagi, Bidar, Raichur, Yadgir, Bellari

## 📁 Project Structure

```
kannada-rajyotsava-site/
├── README.md                     # This file
├── SETUP.md                      # Setup instructions
├── generate_qr.py               # Python script to generate QR codes
├── html/                         # HTML files folder
│   ├── index.html                # Landing page with all regions
│   ├── north-karnataka.html      # North Karnataka (Kittur/Bombay Karnataka)
│   ├── central-karnataka.html    # Central Karnataka (Malnad Region)
│   ├── south-karnataka.html      # South Karnataka (Mysuru Region)
│   ├── coastal.html              # Coastal Karnataka (Karavali/Coastal Belt)
│   ├── southeast-karnataka.html  # South-East Karnataka (Bengaluru/Old Mysore Expansion)
│   └── northeast-karnataka.html  # North-East Karnataka (Kalyana Karnataka)
├── images/                       # Image assets by region
│   ├── north-karnataka/          # North Karnataka images (renamed from bombay-karnataka)
│   ├── central-karnataka/        # Central Karnataka images (renamed from malnad)
│   ├── south-karnataka/          # South Karnataka images (renamed from old-mysore)
│   ├── coastal/                  # Coastal Karnataka images
│   ├── southeast-karnataka/      # South-East Karnataka images (renamed from south-karnataka)
│   └── northeast-karnataka/      # North-East Karnataka images (renamed from hyderabad-karnataka)
├── videos/                       # Video assets by region
│   ├── north-karnataka/          # North Karnataka videos (renamed from bombay-karnataka)
│   ├── central-karnataka/        # Central Karnataka videos (renamed from malnad)
│   ├── south-karnataka/          # South Karnataka videos (renamed from old-mysore)
│   ├── coastal/                  # Coastal Karnataka videos
│   ├── southeast-karnataka/      # South-East Karnataka videos (renamed from south-karnataka)
│   └── northeast-karnataka/      # North-East Karnataka videos (renamed from hyderabad-karnataka)
└── qr_network/                  # Generated QR codes for network access
    ├── index.png
    ├── north-karnataka.png       # North Karnataka QR
    ├── central-karnataka.png     # Central Karnataka QR
    ├── south-karnataka.png       # South Karnataka QR
    ├── coastal.png               # Coastal Karnataka QR
    ├── southeast-karnataka.png   # South-East Karnataka QR
    └── northeast-karnataka.png   # North-East Karnataka QR
```

## 🚀 Quick Start

### 1. Clone/Download the Project
Download all files to your local directory.

### 2. Add Your Media Content
- Place region-specific images in `images/{region-name}/` folders
- Place region-specific videos in `videos/{region-name}/` folders
- Supported formats: JPG, PNG for images; MP4, WebM for videos

### 3. Host on Network & Generate QR Codes
```bash
# Install Python dependencies
pip install qrcode[pil]

# Start the network server
python start_server.py

# Generate network QR codes (in separate terminal)
python generate_qr_network.py
```

### 4. Access the Website
- **Local**: Open `html/index.html` in your web browser
- **Network**: Visit `http://192.168.2.212:8000` or scan QR codes from `qr_network/` folder

## ✨ Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Tailwind CSS Styling**: Modern, festive design with Karnataka flag colors
- **QR Code Integration**: Printable QR codes for easy mobile access
- **Media Support**: Image galleries and video sections for each region
- **Cultural Content**: Authentic descriptions and cultural highlights
- **Interactive Navigation**: Smooth transitions and hover effects

## 🎨 Design Elements

- **Colors**: Red (#DC2626), Yellow (#FBBF24), Gold (#F59E0B) - inspired by Karnataka flag
- **Typography**: Clean, readable fonts with festive text shadows
- **Layout**: Grid-based responsive design with card layouts
- **Icons**: Emoji-based regional representations for instant recognition

## 📱 QR Code Usage

1. **Generate QR codes**: Run `python generate_qr_network.py`
2. **Print QR codes**: Print the generated PNG files from the `qr_network/` folder
3. **Display at event**: Place printed QR codes at your celebration venue
4. **Visitor interaction**: Guests can scan codes to quickly access regional pages

## 🛠️ Customization

### Tismo Branding Complete
All HTML files have been updated with Tismo branding and Second Floor team information for Ethnic Day @ Tismo 2025.

### Add Real Media Content
1. Replace placeholder images in `images/{region}/` folders
2. Replace placeholder videos in `videos/{region}/` folders
3. Update video URLs for YouTube embeds in HTML files

### Modify Content
Each regional HTML file contains:
- Header with region name and description
- About section with 2-3 paragraphs
- Photo gallery grid (6 images)
- Video section (local + YouTube)
- Footer with celebration details

## 🎯 Event Usage Tips

1. **Setup**: Host files on a local web server or share via network drive
2. **Display**: Use projector/TV to showcase the index page
3. **Interaction**: Let visitors explore regions via clicks or QR scans
4. **Printing**: Print QR codes on paper/cards for easy distribution
5. **Social Media**: Share screenshots of regional pages for online promotion

## 🤝 Contributing

To enhance this project:
1. Add more authentic regional content
2. Include additional media files
3. Translate descriptions to Kannada
4. Add audio elements (regional music/songs)
5. Create interactive maps or timelines

## 📝 License

This project is created for educational and cultural celebration purposes. Feel free to modify and use for your office celebrations!

## 🙏 Credits

Created with ❤️ by Tismo's Second Floor Team for celebrating the beautiful diversity of Karnataka.

**Event**: Ethnic Day @ Tismo 2025 – "Festivals of Karnataka"  
**Team**: Second Floor Team  
**Theme**: Kannada Rajyotsava  

**ಕರ್ನಾಟಕದ ಕೀರ್ತಿ ಸದಾ ಬೆಳೆಯಲಿ! | May Karnataka's glory always grow!**

---
*Happy Ethnic Day @ Tismo 2025! 🎉*