from datetime import datetime
import sqlalchemy as sql
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String, nullable=False, unique=True)


class Book(Base):
    __tablename__ = "book"

    id = sql.Column(sql.Integer, primary_key=True, unique=True)
    title = sql.Column(sql.String, nullable=False, primary_key=True)
    id_publisher = sql.Column(sql.Integer, sql.ForeignKey("publisher.id", ondelete='CASCADE'), nullable=False, primary_key=True)

    publisher = relationship(Publisher, backref="book")


class Shop(Base):
    __tablename__ = "shop"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String, nullable=False, unique=True)


class Stock(Base):
    __tablename__ = "stock"

    id_book = sql.Column(sql.Integer, sql.ForeignKey("book.id", ondelete='CASCADE'), nullable=False, primary_key=True)
    id_shop = sql.Column(sql.Integer, sql.ForeignKey("shop.id", ondelete='CASCADE'), nullable=False, primary_key=True)
    id = sql.Column(sql.Integer, primary_key=True, unique=True)
    count = sql.Column(sql.Integer, nullable=False)

    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')


class Sale(Base):
    __tablename__ = "sale"

    id = sql.Column(sql.Integer, primary_key=True)
    price = sql.Column(sql.Float, nullable=False)
    date_sale = sql.Column(sql.Date, nullable=False, default=datetime.now)
    id_stock = sql.Column(sql.Integer, sql.ForeignKey("stock.id", ondelete='CASCADE'), nullable=False)
    count = sql.Column(sql.Integer, nullable=False)

    stock = relationship(Stock, backref='sale')


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)