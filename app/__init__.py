from flask import Flask
from app.routes import ocr_bp

def create_app():
    app = Flask(__name__)
    
    # Configuration settings
    app.config.from_object("config.Config")
    
    # register blueprints
    app.register_blueprint(ocr_bp, url_prefix='/api/v1')
    
    return app