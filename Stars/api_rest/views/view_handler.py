# /home/diaspedro/Desktop/Projetos/StarTransfer/Stars/api_rest/views/view_handler.py

from flask import Flask, request, jsonify
from api_rest.controllers.controller_handler import validar_caminho

app = Flask(__name__)

@app.route('/validate_path', methods=['POST'])
def validate_path():
    try:
        data = request.get_json()
        path = data.get('path', '')
        is_valid = validar_caminho(path)
        return jsonify({'path': path, 'is_valid': is_valid})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
