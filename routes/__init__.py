from flask import Blueprint
from .property_routes import property_bp
from .user_routes import user_bp

def init_routes(app):
    app.register_blueprint(property_bp)
    app.register_blueprint(user_bp)
