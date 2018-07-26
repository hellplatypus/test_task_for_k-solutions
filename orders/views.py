import requests

from flask import Blueprint, render_template, request
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from datetime import datetime

from orders.constants import CURRENCY_RUB, SHOP_ID
from orders.forms import OrdersForm
from orders.utils import generate_sign
from orders.models import Order

orders = Blueprint('orders', __name__)


@orders.route('/', methods=('GET', 'POST'))
def make_order():

    form = OrdersForm()

    if request.method == 'POST':

        if form.validate_on_submit():

            currency = request.form.get("currency")

            if currency == 'RUB':
                # todo
                return abort(403, 'RUB is currently unavailable, please use USD')

            elif currency == 'EUR':
                # todo
                return abort(403, 'EUR is currently unavailable, please use USD')

            elif currency == 'USD':

                request_data = {
                    'shop_amount': request.form.get("amount"),
                    'shop_currency': CURRENCY_RUB,
                    'shop_id': SHOP_ID,
                    'payer_currency': CURRENCY_RUB
                }

                order = Order.create(currency=request_data['shop_currency'],
                                     amount=request_data['shop_amount'],
                                     description=request.form.get("description"),
                                     time=datetime.now())

                request_data['shop_order_id'] = order.id

                request_data['sign'] = generate_sign(**request_data)

                response = requests.post(url='https://core.piastrix.com/bill/create', json=request_data)
                if response.status_code != 200:
                    # show some error message to user
                    return redirect('/')
                else:
                    response = response.json()

                    if 'error_code' in response and response['error_code'] != 0:
                        # show some error message to user
                        return redirect('/')

                return redirect(response['data']['url'])

    return render_template('orders/orders.html', form=form)
