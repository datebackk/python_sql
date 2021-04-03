from sqlA.model import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String, Float, DateTime, Boolean, Date
from sqlalchemy.orm import relationship


class SubjLect(Base):
    __tablename__ = 'subj_lect'

    lecturer_id = Column(Integer, primary_key=True)
    subj_id = Column(Integer)
