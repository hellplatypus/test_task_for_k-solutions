from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('default_settings.py')

    from orders.views import orders
    app.register_blueprint(orders)

    return app
