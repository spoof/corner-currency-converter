from flask import Blueprint, render_template

from currency_converter.forms import ConvertForm

converter_page = Blueprint('converter', __name__)


@converter_page.route('/', methods=['GET', 'POST'])
def index():
    form = ConvertForm()

    return render_template('index.html', form=form)
