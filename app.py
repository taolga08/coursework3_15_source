from flask import Flask

from main.wiews import main_blueprint
from api.wiews import api_blueprint


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = Flask
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def not_found_error(error):
    return 'Страница не найдена', 404


@app.errorhandler(500)
def not_found_error(error):
    return 'Ошибка сервера', 500


if __name__ == '__main__':
    app.run()
