import psycopg2
from dotenv import dotenv_values

def create_structure(connection):
    with connection.cursor() as cur:
        cur.execute("""
        DROP TABLE phone;
        DROP TABLE client;
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(40) UNIQUE NOT NULL,
            last_name VARCHAR(40) UNIQUE NOT NULL,
            email VARCHAR(40) UNIQUE NOT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS phone(
            phone_number VARCHAR(12) PRIMARY KEY,
            client_id INTEGER REFERENCES client(id)
        );
        """)

        connection.commit()

def main():
    config = dotenv_values(".env")
    PASSWORD = config["password"]
    USER = config["username"]
    DATABASE = config["database"]

    with psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD) as connection:
        create_structure(connection)

if __name__ == "__main__":
    main()