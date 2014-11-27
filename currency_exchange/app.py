from flask import Flask

from views.converter import converter_page


app = Flask(__name__)

DEBUG = True
app.config.from_object(__name__)


# register all pages
app.register_blueprint(converter_page)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
