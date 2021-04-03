from sqlA.model import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String, Float, DateTime, Boolean, Date
from sqlalchemy.orm import relationship


class University(Base):
    __tablename__ = 'university'

    univ_id = Column(Integer, primary_key=True)
    univ_name = Column(String(120))
    rating = Column(Integer)
    city = Column(String(120))
