#!/usr/bin/env python3
"""
Configuration settings for Kannada Rajyotsava Flask Application
"""

import os
from pathlib import Path

class Config:
    """Base configuration class"""
    
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kannada-rajyotsava-2025-secure-key'
    
    # Application settings
    DEBUG = False
    TESTING = False
    
    # Server configuration
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 8000))
    
    # Static file configuration
    STATIC_FOLDER = 'html'
    TEMPLATE_FOLDER = 'html'
    
    # File upload settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Security headers
    SECURITY_HEADERS = {
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
        'X-XSS-Protection': '1; mode=block',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'
    }
    
    # Logging configuration
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    
    # Application metadata
    APP_NAME = 'Kannada Rajyotsava Website'
    APP_VERSION = '1.0.0'
    APP_DESCRIPTION = 'Office Cultural Celebration Website for Kannada Rajyotsava 2025'

class DevelopmentConfig(Config):
    """Development configuration"""
    
    DEBUG = True
    PORT = 8000
    
    # Development security headers (less restrictive)
    SECURITY_HEADERS = {
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'SAMEORIGIN',  # Allow embedding in development
        'X-XSS-Protection': '1; mode=block',
        'Cache-Control': 'no-cache'
    }

class ProductionConfig(Config):
    """Production configuration"""
    
    DEBUG = False
    PORT = int(os.environ.get('PORT', 5000))
    
    # Enhanced security for production
    SECURITY_HEADERS = {
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
        'X-XSS-Protection': '1; mode=block',
        'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0',
        'Referrer-Policy': 'strict-origin-when-cross-origin',
        'Content-Security-Policy': "default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'"
    }

class TestingConfig(Config):
    """Testing configuration"""
    
    TESTING = True
    DEBUG = True
    PORT = 8001
    
    # Disable security headers for testing
    SECURITY_HEADERS = {}

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config(config_name=None):
    """Get configuration class by name"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    return config.get(config_name, DevelopmentConfig)