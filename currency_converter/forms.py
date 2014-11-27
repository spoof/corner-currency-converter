from wtforms import Form, FloatField, SelectField, validators


class ConvertForm(Form):

    amount = FloatField('Amount', [validators.InputRequired(),
                                   validators.NumberRange(min=0, max=10000)])
    convert_from = SelectField('From', choices=[('rub', 'RUB'), ('usd', 'USD')])
    convert_to = SelectField('To', choices=[('rub', 'RUB'), ('usd', 'USD')])
