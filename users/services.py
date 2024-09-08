import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(name):
    """ Создаем stripe продукт. """
    product = stripe.Product.create(name=name)
    return product


def create_stripe_price(amount, product_id):
    """Создает цену в Stripe"""
    price = stripe.Price.create(
        currency='usd',
        unit_amount=int(amount) * 100,
        product=product_id,
    )
    return price


def create_stripe_session(price):
    """Создает сессию оплаты в Stripe"""
    session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': price.get('id'),
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return session.get('id'), session.get('url')
