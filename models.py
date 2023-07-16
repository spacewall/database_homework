import sqlalchemy as sql
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Course(Base):
    __tablename__ = "course"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(40), unique=True)

    homework = relationship("Homework", back_populates="course")


class Homework(Base):
    __tablename__ = "homework"

    id = sql.Column(sql.Integer, primary_key=True)
    number = sql.Column(sql.Integer, nulable=False)
    description = sql.Column(sql.Text, nullable=False)
    curse_id = sql.Column(sql.Integer, sql.ForeignKey("course.id"), nullable=False)

    course = relationship(Course, back_populates="homeworks")
