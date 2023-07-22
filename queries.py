import sqlalchemy
import json
from pprint import pprint
from models import create_tables, Publisher, Book, Shop, Stock, Sale
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

def push_data(session):
    with open('tests_data.json', 'r') as raw_data:
        data = json.load(raw_data)

    for record in data:
        model = {
            'publisher': Publisher,
            'book': Book,
            'shop': Shop,
            'stock': Stock,
            'sale': Sale
        }[record['model']]

        session.add(model(id=record['pk'], **record['fields']))

    session.commit()

def get_info_by_publisher(session, name):
    id = session.query(Publisher.id).filter(Publisher.name == name).one_or_none()

    if id == None:
        print(f'There is no {name}, check another publisher')
    else:
        for title, book_id in session.query(Book.title, Book.id).filter(Book.id_publisher == id[0]).all():
            for stock_id, shop_id in session.query(Stock.id, Stock.id_shop).filter(Stock.id_book == book_id).all():
                shop = session.query(Shop.name).filter(Shop.id == shop_id).one()[0]
                price_and_date = session.query(Sale.price, Sale.date_sale).filter(Sale.id_stock == stock_id).all()
                if price_and_date != []:
                    price = price_and_date[0][0]
                    date = str(price_and_date[0][1])
                    print(f'{title} | {shop} | {price} | {date}')
                    

def main(publisher):
    config = dotenv_values(".env")
    LOGIN = config["username"]
    PASSWORD = config["password"]
    DATABASE = config["database"]
    data_source_name = f'postgresql://{LOGIN}:{PASSWORD}@localhost:5432/{DATABASE}'
    engine = sqlalchemy.create_engine(data_source_name)

    create_tables(engine)

    Session = sessionmaker(engine)

    with Session() as session:
        push_data(session)
        get_info_by_publisher(session, publisher)

if __name__ == '__main__':
    publisher_name = ...
    main(publisher_name)
