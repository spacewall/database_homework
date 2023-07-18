import sqlalchemy as sql
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Course(Base):
    __tablename__ = "course"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(40), unique=True)

    homework = relationship("Homework", back_populates="course")

    def __str__(self):
        return f'Course {self.id}: {self.name}'
    

class Homework(Base):
    __tablename__ = "homework"

    id = sql.Column(sql.Integer, primary_key=True)
    number = sql.Column(sql.Integer, nullable=False)
    description = sql.Column(sql.Text, nullable=False)
    course_id = sql.Column(sql.Integer, sql.ForeignKey("course.id"), nullable=False)

    # course = relationship(Course, back_populates="homeworks")
    course = relationship(Course, backref="homeworks")

    def __str__(self):
        return f"Homework {self.id}: ({self.number}, {self.description}, {self.course})"
    


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
