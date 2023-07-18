import sqlalchemy
from models import create_tables, Course, Homework
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config = dotenv_values(".env")
LOGIN = config["username"]
PASSWORD = config["password"]
DATABASE = config["database"]
data_source_name = f'postgresql://{LOGIN}:{PASSWORD}@localhost:5432/{DATABASE}'
engine = sqlalchemy.create_engine(data_source_name)

create_tables(engine)

Session = sessionmaker(engine)
session = Session()

course_1 = Course(name='Python')

session.add(course_1)
session.commit()

print(course_1)

homework_1 = Homework(number=1, description='простая домашняя работа', course=course_1)

homework_2 = Homework(number=2, description='сложная домашняя работа', course=course_1)
session.add_all([homework_1, homework_2])
session.commit()

for homework in session.query(Homework).filter(Homework.description.like('%сложн%')).all():
    print(homework)

for course in session.query(Course).join(Homework.course).filter(Homework.number == 1).all():
    print(course)

course_2 = Course(name='Java')
session.add(course_2)
session.commit()

subquery = session.query(Homework).filter(Homework.description.like('%сложн%')).subquery()
for course in session.query(Course).join(subquery, Course.id == subquery.c.course_id):
    print(course)

session.query(Course).filter(Course.name == 'Java').update({'name': 'JavaScript'})
session.commit()

session.query(Course).filter(Course.name == 'JavaScript').delete()
session.commit()

for course in session.query(Course).all():
    print(course)

session.close()