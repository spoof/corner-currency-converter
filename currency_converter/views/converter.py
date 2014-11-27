from flask import Blueprint, render_template, request

from currency_converter.forms import ConvertForm

converter_page = Blueprint('converter', __name__)


@converter_page.route('/', methods=['GET', 'POST'])
def index():
    form = ConvertForm(request.form)
    result = None
    if request.method == 'POST' and form.validate():
        result = 'result'
    return render_template('index.html', form=form, result=result)
