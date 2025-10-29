#!/usr/bin/env python3
"""
Flask Application for Kannada Rajyotsava Website
Pure Flask implementation without websockets
"""

from flask import Flask, send_from_directory, request, jsonify, g
from pathlib import Path
import socket
import logging
import os
from datetime import datetime
from werkzeug.exceptions import NotFound, InternalServerError

def create_app(config_name='development'):
    """Application factory function"""
    app = Flask(__name__)
    
    # Load configuration
    from config import config
    app.config.from_object(config[config_name])
    
    # Setup logging
    setup_logging(app)
    
    # Register components
    register_routes(app)
    register_error_handlers(app)
    register_middleware(app)
    
    return app

def setup_logging(app):
    """Setup application logging"""
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        
        file_handler = logging.FileHandler('logs/kannada_rajyotsava.log')
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Kannada Rajyotsava website startup')

def register_routes(app):
    """Register application routes"""
    
    # Define directories
    html_dir = Path(__file__).parent / "html"
    images_dir = Path(__file__).parent / "images"
    videos_dir = Path(__file__).parent / "videos"
    qr_dir = Path(__file__).parent / "qr_network"
    
    @app.route('/')
    def index():
        """Serve the main index page"""
        try:
            return send_from_directory(html_dir, 'index.html')
        except FileNotFoundError:
            return "Welcome to Kannada Rajyotsava 2025! 🎉<br>ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ೨೦೨೫", 200
    
    # Regional pages routes
    @app.route('/north-karnataka.html')
    def north_karnataka():
        """Serve North Karnataka page"""
        return send_from_directory(html_dir, 'north-karnataka.html')
    
    @app.route('/central-karnataka.html')
    def central_karnataka():
        """Serve Central Karnataka page"""
        return send_from_directory(html_dir, 'central-karnataka.html')
    
    @app.route('/south-karnataka.html')
    def south_karnataka():
        """Serve South Karnataka page"""
        return send_from_directory(html_dir, 'south-karnataka.html')
    
    @app.route('/coastal.html')
    def coastal():
        """Serve Coastal Karnataka page"""
        return send_from_directory(html_dir, 'coastal.html')
    
    @app.route('/southeast-karnataka.html')
    def southeast_karnataka():
        """Serve Southeast Karnataka page"""
        return send_from_directory(html_dir, 'southeast-karnataka.html')
    
    @app.route('/northeast-karnataka.html')
    def northeast_karnataka():
        """Serve Northeast Karnataka page"""
        return send_from_directory(html_dir, 'northeast-karnataka.html')
    
    # Static file routes
    @app.route('/styles.css')
    def styles():
        """Serve CSS files"""
        return send_from_directory(html_dir, 'styles.css')
    
    @app.route('/tailwind.min.css')
    def tailwind():
        """Serve Tailwind CSS"""
        return send_from_directory(html_dir, 'tailwind.min.css')
    
    @app.route('/images/<path:filename>')
    def serve_images(filename):
        """Serve image files"""
        # Security check - prevent directory traversal
        if '..' in filename or filename.startswith('/'):
            return "Access denied", 403
        return send_from_directory(images_dir, filename)
    
    @app.route('/videos/<path:filename>')
    def serve_videos(filename):
        """Serve video files"""
        # Security check - prevent directory traversal
        if '..' in filename or filename.startswith('/'):
            return "Access denied", 403
        return send_from_directory(videos_dir, filename)
    
    @app.route('/qr_network/<path:filename>')
    def serve_qr_codes(filename):
        """Serve QR code files"""
        # Security check - prevent directory traversal
        if '..' in filename or filename.startswith('/'):
            return "Access denied", 403
        return send_from_directory(qr_dir, filename)
    
    # API endpoints
    @app.route('/api/health')
    def health_check():
        """Health check endpoint"""
        return jsonify({
            "status": "healthy",
            "service": "Kannada Rajyotsava Website",
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0"
        })
    
    @app.route('/api/info')
    def server_info():
        """Server information endpoint"""
        local_ip = get_local_ip()
        return jsonify({
            "server_ip": local_ip,
            "port": request.environ.get('SERVER_PORT', '8000'),
            "host": request.host,
            "user_agent": request.headers.get('User-Agent'),
            "timestamp": datetime.now().isoformat()
        })
    
    # Generic file serving (fallback)
    @app.route('/<path:filename>')
    def serve_file(filename):
        """Generic file serving with security checks"""
        # Security check - prevent directory traversal
        if '..' in filename or filename.startswith('/'):
            return "Access denied", 403
        
        # Try to serve from html directory first
        try:
            return send_from_directory(html_dir, filename)
        except FileNotFoundError:
            # If not found in html, return 404
            return "File not found", 404

def register_error_handlers(app):
    """Register error handlers"""
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return jsonify({
            "error": "Page not found",
            "message": "The requested page does not exist",
            "kannada": "ಈ ಪುಟ ಲಭ್ಯವಿಲ್ಲ"
        }), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors"""
        return jsonify({
            "error": "Internal server error",
            "message": "Something went wrong on our end",
            "kannada": "ಆಂತರಿಕ ದೋಷ ಸಂಭವಿಸಿದೆ"
        }), 500
    
    @app.errorhandler(403)
    def forbidden(error):
        """Handle 403 errors"""
        return jsonify({
            "error": "Access forbidden",
            "message": "You don't have permission to access this resource",
            "kannada": "ಪ್ರವೇಶ ನಿಷೇಧಿಸಲಾಗಿದೆ"
        }), 403

def register_middleware(app):
    """Register middleware functions"""
    
    @app.before_request
    def log_request_info():
        """Log request information"""
        g.start_time = datetime.now()
        app.logger.info(f'{request.remote_addr} - {request.method} {request.url}')
    
    @app.after_request
    def add_security_headers(response):
        """Add security headers to all responses"""
        # Security headers from config
        for header, value in app.config.get('SECURITY_HEADERS', {}).items():
            response.headers[header] = value
        
        # CORS headers for API endpoints
        if request.path.startswith('/api/'):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        
        # Log response time
        if hasattr(g, 'start_time'):
            duration = datetime.now() - g.start_time
            app.logger.info(f'Request completed in {duration.total_seconds():.3f}s')
        
        return response

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "localhost"

def print_startup_info(app, host, port):
    """Print startup information"""
    local_ip = get_local_ip()
    
    print("🌐 Kannada Rajyotsava Flask Server Starting...")
    print(f"🔗 Local access: http://localhost:{port}")
    print(f"🔗 Network access: http://{local_ip}:{port}")
    print(f"📱 Mobile devices on same network can access via: http://{local_ip}:{port}")
    print(f"📁 Serving files from: {Path(__file__).parent / 'html'}")
    print("\n🎯 Available pages:")
    print(f"   • Main page: http://{local_ip}:{port}/")
    print(f"   • North Karnataka: http://{local_ip}:{port}/north-karnataka.html")
    print(f"   • Central Karnataka: http://{local_ip}:{port}/central-karnataka.html")
    print(f"   • South Karnataka: http://{local_ip}:{port}/south-karnataka.html")
    print(f"   • Coastal Karnataka: http://{local_ip}:{port}/coastal.html")
    print(f"   • South-East Karnataka: http://{local_ip}:{port}/southeast-karnataka.html")
    print(f"   • North-East Karnataka: http://{local_ip}:{port}/northeast-karnataka.html")
    print("\n🔧 API Endpoints:")
    print(f"   • Health check: http://{local_ip}:{port}/api/health")
    print(f"   • Server info: http://{local_ip}:{port}/api/info")
    print("\n💡 Instructions:")
    print("   1. Make sure all devices are on the same WiFi network")
    print("   2. Generate QR codes using: python generate_qr.py")
    print("   3. Print and display QR codes at your event")
    print("   4. Visitors can scan QR codes to access pages")
    print("\n🛑 Press Ctrl+C to stop the server")
    print("=" * 70)

if __name__ == "__main__":
    # Create Flask app
    app = create_app('development')
    
    host = app.config.get('HOST', '0.0.0.0')
    port = app.config.get('PORT', 8000)
    debug = app.config.get('DEBUG', True)
    
    # Print startup information
    print_startup_info(app, host, port)
    
    # Run the application
    app.run(host=host, port=port, debug=debug, threaded=True)