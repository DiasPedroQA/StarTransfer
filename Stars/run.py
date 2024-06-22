from api_rest import create_app

api_rest = create_app()

if __name__ == '__main__':
    api_rest.run(debug=True)
