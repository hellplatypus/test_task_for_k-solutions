from flask import Blueprint, abort
from jinja2 import TemplateNotFound


orders = Blueprint('orders', __name__)


@orders.route('/')
def show():
    try:
        return 'init commit'
    except TemplateNotFound:
        abort(404)
