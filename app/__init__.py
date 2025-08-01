from flask import Flask
from config import Config
from app.routes import main_bp
from app.routes.dashboard_route import dashboard_bp
from app.routes.prediksi_route import prediksi_bp
from app.routes.monitoring_route import monitoring_bp
from app.routes.chatbot_route import chatbot_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import dan register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(prediksi_bp)
    app.register_blueprint(monitoring_bp)
    app.register_blueprint(chatbot_bp)

    return app

# Create app instance
app = create_app()