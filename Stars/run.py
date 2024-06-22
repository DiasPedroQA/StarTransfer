from api_rest import create_app
from loguru import logger

app = create_app()

if __name__ == '__main__':
    logger.info("Iniciando a aplicação...")
    app.run(debug=True)
