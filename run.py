import os

from app import create_app


config_name = os.getenv('FLASK_CONFIG')
config_name = 'development'
app = create_app(config_name)
os.path.dirname(os.path.dirname(__file__))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port='5000', host='0.0.0.0')

