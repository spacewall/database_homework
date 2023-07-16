import sqlalchemy
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config = dotenv_values(".env")
LOGIN = config["username"]
PASSWORD = config["password"]
data_source_name = f'postgresql://{LOGIN}:{PASSWORD}@localhost:5432/postgres'

engine = sqlalchemy.create_engine(data_source_name)
Session = sessionmaker(engine)
session = Session()

session.close()