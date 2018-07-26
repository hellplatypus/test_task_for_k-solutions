import requests

from flask import Blueprint, render_template, request
from werkzeug.utils import redirect

from orders.constants import CURRENCY_RUB, SHOP_ID
from orders.forms import OrdersForm
from orders.utils import generate_sign, get_order_id

orders = Blueprint('orders', __name__)


@orders.route('/', methods=('GET', 'POST'))
def order():

    form = OrdersForm()

    if request.method == 'POST':

        if form.validate_on_submit():

            currency = request.form.get("currency")

            if currency == 'RUB':
                return redirect('/')

            elif currency == 'EUR':
                return redirect('/')

            elif currency == 'USD':

                request_data = {
                    'shop_amount': request.form.get("amount"),
                    'shop_currency': CURRENCY_RUB,
                    'shop_id': SHOP_ID,
                    'shop_order_id': get_order_id(),
                    'payer_currency': CURRENCY_RUB
                }

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
