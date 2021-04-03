from sqlA.model import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Float, DateTime, Boolean, Date
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = 'student'

    student_id = Column(Integer, primary_key=True)
    surname = Column(String(120))
    name = Column(String(120))
    stipend = Column(Integer)
    kurs = Column(Integer)
    city = Column(String(120))
    birthday = Column(Date)
    univ_id = Column(Integer, ForeignKey('university.univ_id'))
    univ = relationship('University')
