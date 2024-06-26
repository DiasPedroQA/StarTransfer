from flask import Flask, request, jsonify
from Stars.api_rest.controllers.handler import validar_caminho


app = Flask(__name__)


@app.route('/validar_caminho', methods=['POST'])
def validar_caminho_api():
    try:
        data = request.get_json()
        path = data.get('path', '')
        is_valid = validar_caminho(path)
        return jsonify({'path': path, 'is_valid': is_valid})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
