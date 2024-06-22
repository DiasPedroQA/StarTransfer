from importlib.metadata import version as package_version

werkzeug_version = package_version("werkzeug")

# Use werkzeug_version conforme necessário no restante do seu código

from flask import Flask
from loguru import logger

def create_app():
    app = Flask(__name__)

    # Configuração do logger
    logger.add("logs/info.log", rotation="1 day", retention="7 days", level="INFO",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")

    from .views import main_bp
    app.register_blueprint(main_bp)

    return app
