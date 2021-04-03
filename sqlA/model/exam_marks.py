from sqlA.model import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String, Float, DateTime, Boolean, Date
from sqlalchemy.orm import relationship


class ExamMarks(Base):
    __tablename__ = 'exam_marks'

    exam_id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    subj_id = Column(Integer)
    mark = Column(Integer)
    exam_date = Column(Date)
