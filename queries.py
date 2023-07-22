import sqlalchemy
import json
from pprint import pprint
from models import create_tables, Publisher, Book, Shop, Stock, Sale
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

def push_data(session):
    with open('tests_data.json') as raw_data:
        data = json.dump(raw_data)
    pprint(data)

def main():
    config = dotenv_values(".env")
    LOGIN = config["username"]
    PASSWORD = config["password"]
    DATABASE = config["database"]
    data_source_name = f'postgresql://{LOGIN}:{PASSWORD}@localhost:5432/{DATABASE}'
    engine = sqlalchemy.create_engine(data_source_name)

    create_tables(engine)

    with sessionmaker(engine) as session:
        push_data(session)

if __name__ == '__main__':
    main()
