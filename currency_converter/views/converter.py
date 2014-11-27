from decimal import Decimal

from flask import Blueprint, render_template, request

from currency_converter.forms import ConvertForm
from currency_converter.app import redis_store

converter_page = Blueprint('converter', __name__)

BASE_CURRENCY = 'RUB'


@converter_page.route('/', methods=['GET', 'POST'])
def index():
    form = ConvertForm(request.form)

    # it's a bad way to cache all available currencies. But it's ok for this
    # example
    currency_choices = redis_store.keys('*') or []
    currency_choices = [(c, c) for c in sorted(currency_choices)]
    currency_choices.insert(0, (BASE_CURRENCY, BASE_CURRENCY))
    form.convert_from.choices = currency_choices
    form.convert_to.choices = currency_choices

    result = None
    if request.method == 'POST' and form.validate():
        from_currency = form.convert_from.data.upper()
        to_currency = form.convert_to.data.upper()
        amount = Decimal(form.amount.data)

        if from_currency == to_currency:
            result = amount
        else:
            base_amount = amount
            if from_currency != BASE_CURRENCY:
                from_currency_data = redis_store.hgetall(from_currency)
                base_amount = amount * Decimal(from_currency_data['rate'])

            rate = Decimal(1.0)
            if to_currency != BASE_CURRENCY:
                to_currency_data = redis_store.hgetall(to_currency)
                rate = rate / Decimal(to_currency_data['rate'])

            result = base_amount * rate
            result = result.quantize(Decimal('.0000'))

    return render_template('index.html', form=form, result=result)
