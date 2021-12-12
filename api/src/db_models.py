from db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String)
    blocked = Column(Boolean)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    hashtags = Column(String)
    type = Column(String)
    category = Column(String)
    exams = Column(Integer)
    suscription = Column(String)
    location = Column(String)
    creator = Column(Integer)
    enrollment_conditions = Column(String)
    unenrollment_conditions = Column(String)


class Inscription(Base):
    __tablename__ = 'inscriptions'
    idcourse= Column(Integer, ForeignKey(Course.id), primary_key=True)
    idstudent = Column(Integer, ForeignKey(User.id), primary_key=True)
