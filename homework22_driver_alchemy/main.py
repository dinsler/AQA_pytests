from sqlalchemy.orm import Session
from sqlalchemy import select

from db.models import Product, Order
from session import __engine


def execute_query():
    with Session(__engine) as session:
        data = session.execute(
            select(
                Product.name,
                Product.price,
                Order.quantity,
                (Product.price * Order.quantity).label("total")
            ).where(Product.id == Order.product_id)).all()
        for p in data:
            print(p)


if __name__ == '__main__':
    execute_query()
