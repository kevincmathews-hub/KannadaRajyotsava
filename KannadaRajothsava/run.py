#!/usr/bin/env python3
"""
Simple run script for Kannada Rajyotsava Flask Application
Alternative to main.py with additional options
"""

import os
import sys
import argparse
from app import create_app, get_local_ip

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Kannada Rajyotsava Website Server')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=8000, help='Port to bind to (default: 8000)')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--config', choices=['development', 'production', 'testing'], 
                       default='development', help='Configuration to use')
    return parser.parse_args()

def main():
    """Main function to run the Flask application"""
    args = parse_arguments()
    
    # Set environment variables from arguments
    os.environ['FLASK_ENV'] = args.config
    if args.port != 8000:
        os.environ['PORT'] = str(args.port)
    
    # Create Flask app
    app = create_app(args.config)
    
    # Override config with command line arguments
    host = args.host
    port = args.port
    debug = args.debug or app.config.get('DEBUG', False)
    
    # Print startup information
    local_ip = get_local_ip()
    print("🌐 Kannada Rajyotsava Flask Server")
    print(f"📊 Configuration: {args.config}")
    print(f"🔗 Local access: http://localhost:{port}")
    print(f"🔗 Network access: http://{local_ip}:{port}")
    print(f"🐛 Debug mode: {'Enabled' if debug else 'Disabled'}")
    print("=" * 50)
    
    try:
        # Run the Flask application
        app.run(
            host=host,
            port=port,
            debug=debug,
            threaded=True,
            use_reloader=debug
        )
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        print("✅ Thank you for celebrating Kannada Rajyotsava!")
        print("   ಧನ್ಯವಾದಗಳು! | Thank you!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()