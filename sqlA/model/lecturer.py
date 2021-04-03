from sqlA.model import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String, Float, DateTime, Boolean, Date
from sqlalchemy.orm import relationship


class Lecturer(Base):
    __tablename__ = 'lecturer'

    lecturer_id = Column(Integer, primary_key=True)
    surname = Column(String(120))
    name = Column(String(120))
    city = Column(String(120))
    univ_id = Column(Integer)
