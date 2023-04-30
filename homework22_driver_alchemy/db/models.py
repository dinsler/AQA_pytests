from sqlalchemy import Column, INTEGER, Float, VARCHAR, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, relationship

from homework22_driver_alchemy.session import __engine

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(INTEGER, nullable=False, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    price = Column(Float, nullable=True)

    orders = relationship("Order", back_populates="product", cascade="all, delete-orphan")

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, price: {self.price}"


class Order(Base):
    __tablename__ = 'orders'

    id = Column(INTEGER, nullable=False, primary_key=True)
    product_id = Column(INTEGER, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="orders")

    def __str__(self):
        return f"id: {self.id}, product_id: {self.product_id}, quantity: {self.quantity}"


Base.metadata.create_all(__engine)
