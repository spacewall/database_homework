import psycopg2
from dotenv import dotenv_values

def create_structure(connection):
    with connection.cursor() as cur:
        # Для обновления таблиц
        cur.execute("""
        DROP TABLE phone;
        DROP TABLE client;
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(40) NOT NULL,
            last_name VARCHAR(40) NOT NULL,
            email VARCHAR(40) UNIQUE NOT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS phone(
            phone_number VARCHAR(12) PRIMARY KEY,
            client_id INTEGER REFERENCES client(id) NOT NULL
        );
        """)

    connection.commit()

def add_client(connection, first_name, last_name, email):
    # Добавим слиента по email (уникальный)
    with connection.cursor() as cur:
        cur.execute("""
        INSERT INTO client(first_name, last_name, email) VALUES(%s, %s, %s);""", (first_name, last_name, email)
        )

    connection.commit()
        
def check_table(connection):
    """Функция проверки базы"""
    
    with connection.cursor() as cur:
        cur.execute("""
        SELECT * FROM client;""")
        
        print(cur.fetchall())

        cur.execute("""
        SELECT * FROM phone;""")
        
        print(cur.fetchall())

def add_phone_number(connection, email, number):
    # Поиск осуществляется по уникальному полю
    with connection.cursor() as cur:
        cur.execute("""
        INSERT INTO phone VALUES(%s, (SELECT id FROM client
        WHERE email = %s));""", (number, email)
        )

    connection.commit()

def update_client_info(connection, email, new_first_name=None, new_last_name=None, new_email=None):
    with connection.cursor() as cur:
        cur.execute("""
        SELECT first_name, last_name, email FROM client 
        WHERE email = %s;""", (email, )
        )

        first_name, last_name, _ = cur.fetchall()[0]

        if new_first_name not in (None, first_name):
            cur.execute("""
            UPDATE client SET first_name = %s WHERE email = %s;""", 
            (new_first_name, email)
            )
        if new_last_name not in (None, last_name):
            cur.execute("""
            UPDATE client SET last_name = %s WHERE email = %s;""", 
            (new_last_name, email)
            )
        if new_email not in (None, email):
            cur.execute("""
            UPDATE client SET email = %s WHERE email = %s;""", 
            (new_email, email)
            )

    connection.commit()

def remove_phone_number(connection, number):
    # Так как один телефон не может принадлежать нескольким пользователям, номер телефона уникален, id пользователя знать не обязательно
    with connection.cursor() as cur:
        cur.execute("""
        DELETE FROM phone WHERE phone_number = %s;
        """, (number,)
        )

    connection.commit()

def remove_client_info(connection, first_name, last_name, email):
    with connection.cursor() as cur:
        cur.execute("""
        DELETE FROM phone WHERE client_id = (SELECT id FROM client WHERE first_name = %s AND last_name = %s AND email = %s);""", (first_name, last_name, email)
        )

        cur.execute("""
        DELETE FROM client WHERE first_name = %s AND last_name = %s AND email = %s;""", (first_name, last_name, email)
        )
        
    connection.commit()

def search_client(connection, first_name='%', last_name='%', email='%', number='%'):
    # В задании написано найти пользователя, поэтому в контексте своей реализации под этим понимается найти уникальный id клиента, зная его, можно всегда вытащить и атрибуты других полей конструкцией JOIN
    with connection.cursor() as cur:
        # По данным пользователя
        cur.execute("""
        SELECT first_name, last_name, email FROM client 
        WHERE first_name = %s OR last_name = %s OR email = %s;""", (first_name, last_name, email)
        )
        
        print(cur.fetchall())
        
        # По номеру телефона
        cur.execute("""
        SELECT first_name, last_name, email FROM client c JOIN (SELECT client_id FROM phone 
        WHERE phone_number = %s) t ON c.id = t.client_id;""", (number,)
        )
        
        print(cur.fetchall())

def main():
    config = dotenv_values(".env")
    PASSWORD = config["password"]
    USER = config["username"]
    DATABASE = config["database"]

    with psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD) as connection:
        create_structure(connection)
        # first_name = input("First name: ")
        # last_name = input("Last name: ")
        # email = input("Email: ")
        # number = input("Phone number: ")

        first_name = "Adam"
        last_name = "Po"
        email = "podam@oiate.ru"
        number = "+78005553535"

        add_client(connection, first_name, last_name, email)
        add_phone_number(connection, email, number)
        # remove_phone_number(connection, email, number)

        new_first_name = "Swimmer"
        new_last_name = "Peaty"
        email = "podam@oiate.ru"
        new_email = "peadam@oiate.ru"

        update_client_info(connection, email=email, new_last_name=new_last_name, new_email=email)
        # remove_client_info(connection, first_name, last_name, email)
        add_client(connection, first_name, last_name, new_email)
        # search_client(connection, first_name, "Po", email, number)
        check_table(connection)

if __name__ == "__main__":
    main()
