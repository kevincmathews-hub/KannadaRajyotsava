# Kannada Rajyotsava Flask Website

🎉 **ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ೨೦೨೫** - Pure Flask Web Application

A Flask-based website for celebrating Kannada Rajyotsava in your office or organization. This project has been **migrated from HTTP server to pure Flask** implementation.

## 🚀 Quick Start

### Option 1: Automated Setup (Windows)
```batch
run_flask.bat
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Generate QR codes
python generate_qr.py

# Start Flask server
python main.py
```

### Option 3: Advanced Setup
```bash
# Using setup script
python setup.py

# Using run script with options
python run.py --host 0.0.0.0 --port 8000 --debug

# Using Flask CLI
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --host=0.0.0.0 --port=8000
```

## 📂 Project Structure

```
KannadaRajothsava/
├── app.py              # Flask application factory
├── config.py           # Configuration settings
├── main.py             # Main entry point
├── run.py              # Alternative run script
├── setup.py            # Automated setup script
├── generate_qr.py      # QR code generator
├── requirements.txt    # Python dependencies
├── run_flask.bat       # Windows batch file
├── html/               # Web pages
│   ├── index.html
│   ├── north-karnataka.html
│   ├── central-karnataka.html
│   ├── south-karnataka.html
│   ├── coastal.html
│   ├── southeast-karnataka.html
│   ├── northeast-karnataka.html
│   └── styles.css
├── images/             # Image assets
├── videos/             # Video assets
└── qr_network/         # Generated QR codes
```

## 🌐 Flask Features

- **Pure Flask Implementation**: No websockets, simple HTTP server
- **Application Factory Pattern**: Modular and configurable
- **Security Headers**: XSS protection, content type options
- **Error Handling**: Custom 404 and 500 error pages
- **API Endpoints**: Health check and server info
- **Static File Serving**: Images, videos, CSS files
- **Configuration Management**: Development and production configs
- **Logging**: Request logging and error tracking

## 📱 Network Access

1. **Start the server** using any method above
2. **Generate QR codes** with `python generate_qr.py`
3. **Print QR codes** from the `qr_network/` folder
4. **Share QR codes** at your event
5. **Visitors scan** QR codes to access on mobile devices

## 🔧 Configuration

### Environment Variables
```bash
# Configuration mode
set FLASK_ENV=development      # or production
set FLASK_APP=app.py

# Server configuration
set HOST=0.0.0.0
set PORT=8000

# Security
set SECRET_KEY=your-secret-key
```

### Configuration Files
- `config.py` - Main configuration
- `DevelopmentConfig` - Debug enabled, relaxed security
- `ProductionConfig` - Debug disabled, enhanced security

## 🛠️ Development

### Running in Development Mode
```bash
python main.py
# or
python run.py --debug
# or
set FLASK_ENV=development && flask run --host=0.0.0.0 --port=8000
```

### Running in Production Mode
```bash
set FLASK_ENV=production
python main.py
# or
python run.py --config production
```

## 📊 API Endpoints

- `GET /api/health` - Health check
- `GET /api/info` - Server information
- `GET /` - Main page
- `GET /<region>.html` - Regional pages
- `GET /images/<path>` - Image files
- `GET /videos/<path>` - Video files
- `GET /qr_network/<path>` - QR code files

## 🔒 Security Features

- Directory traversal protection
- Security headers (XSS, CSRF, Content-Type)
- Input validation
- Error handling
- Request logging
- CORS support for API endpoints

## 🎯 Regional Pages

- **North Karnataka** (`/north-karnataka.html`)
- **Central Karnataka** (`/central-karnataka.html`)
- **South Karnataka** (`/south-karnataka.html`)
- **Coastal Karnataka** (`/coastal.html`)
- **Southeast Karnataka** (`/southeast-karnataka.html`)
- **Northeast Karnataka** (`/northeast-karnataka.html`)

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use different port
python run.py --port 8080
# or
set PORT=8080 && python main.py
```

### IP Address Changes
```bash
# Regenerate QR codes
python generate_qr.py
```

### Dependencies Issues
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📦 Dependencies

- **Flask 3.1.2** - Web framework
- **Werkzeug 3.1.3** - WSGI utility library
- **qrcode[pil] 7.4.2** - QR code generation
- **Pillow ≥10.0.0** - Image processing

## 🎉 Migration from HTTP Server

This project has been successfully migrated from a simple HTTP server to a full Flask application with the following improvements:

- ✅ **Application Factory Pattern**
- ✅ **Configuration Management**
- ✅ **Error Handling**
- ✅ **Security Headers**
- ✅ **API Endpoints**
- ✅ **Request Logging**
- ✅ **Modular Structure**
- ✅ **No Websockets** (Pure Flask)

## 🤝 Contributing

Feel free to enhance this project for your Kannada Rajyotsava celebrations!

---

**ಕರ್ನಾಟಕದ ಕೀರ್ತಿ ಸದಾ ಬೆಳೆಯಲಿ!** | *May Karnataka's glory always grow!*