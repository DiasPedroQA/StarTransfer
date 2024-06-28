import os
import sys

# Adicionar o diretório raiz do projeto ao sys.path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), "../../"
        )
    )
)
