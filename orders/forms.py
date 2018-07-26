from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange


class OrdersForm(FlaskForm):

    amount = IntegerField('Cost', validators=[DataRequired(), NumberRange(min=0)])
    currency = SelectField('Currency', choices=[('RUB', 'RUB'), ('EUR', 'EUR'), ('USD', 'USD')])
    description = TextAreaField('Description', validators=[DataRequired()])

