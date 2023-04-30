import json
from pathlib import Path

from sqlalchemy.orm import Session
from sqlalchemy import select

from homework22_driver_alchemy.db.models import Product, Order
from homework22_driver_alchemy.session import __engine


def add_data():
    fp = Path('dummy_data/product.json').read_text()
    product_data = json.loads(fp)
    orders_fp = Path('dummy_data/orders.json').read_text()
    orders_data = json.loads(orders_fp)

    product_data_objects = []
    order_data_objects = []

    for name, values in product_data.items():
        price = values.get('price')
        product_data_objects.append(Product(name=name, price=price))

    query = select(Product)

    with Session(__engine) as session:
        session.add_all(product_data_objects)
        session.commit()

        products_q_data = session.scalars(query).all()
        for product in products_q_data:
            quantity = orders_data.get(product.name).get('quantity')
            order_data_objects.append(Order(product_id=product.id, quantity=quantity))

        session.add_all(order_data_objects)
        session.commit()


if __name__ == '__main__':

    add_data()
