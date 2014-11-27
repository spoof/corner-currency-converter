from flask import Blueprint, render_template

converter_page = Blueprint('converter', __name__)


@converter_page.route('/')
def index():
    return render_template('index.html')
