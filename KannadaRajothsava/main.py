#!/usr/bin/env python3
"""
Main entry point for Kannada Rajyotsava Flask Application
Pure Flask implementation - no websockets
"""

import os
import sys
from app import create_app, get_local_ip, print_startup_info

def main():
    """Main function to run the Flask application"""
    
    # Get configuration from environment
    config_name = os.environ.get('FLASK_ENV', 'development')
    
    # Create Flask app using factory pattern
    app = create_app(config_name)
    
    # Get configuration
    host = app.config.get('HOST', '0.0.0.0')
    port = app.config.get('PORT', 8000)
    debug = app.config.get('DEBUG', True)
    
    # Print startup information
    print_startup_info(app, host, port)
    
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
        print("✅ Thank you for celebrating Kannada Rajyotsava with us!")
        print("   ಧನ್ಯವಾದಗಳು! | Thank you!")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\n❌ Error: Port {port} is already in use!")
            print("   Solutions:")
            print("   1. Close other applications using this port")
            print("   2. Use a different port: set PORT=8080 && python main.py")
            print("   3. Kill the process using the port")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
