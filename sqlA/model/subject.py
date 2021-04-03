from sqlA.model import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String, Float, DateTime, Boolean, Date
from sqlalchemy.orm import relationship


class Subject(Base):
    __tablename__ = 'subject'

    subj_id = Column(Integer, primary_key=True)
    subj_name = Column(String(120))
    hour = Column(Integer)
    semester = Column(Integer)
