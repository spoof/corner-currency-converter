from flask import Flask
from flask_redis import Redis

redis_store = Redis()


def create_app():
    app = Flask(__name__)
    app.config.from_object('currency_converter.appconfig.Config')

    redis_store.init_app(app)

    # register all pages
    from views.converter import converter_page

    app.register_blueprint(converter_page)

    return app
