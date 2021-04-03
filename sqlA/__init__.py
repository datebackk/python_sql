# SqlAlchemy__________________________
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import and_
from sqlalchemy.dialects import postgresql

# Models______________________________
from sqlA.model.exam_marks import ExamMarks
from sqlA.model.lecturer import Lecturer
from sqlA.model.student import Student
from sqlA.model.subj_lect import SubjLect
from sqlA.model.subject import Subject
from sqlA.model.university import University


SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/python_sql'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
session = sessionmaker(bind=engine)()

# s1 = session.query(Student).filter(and_(Student.student_id == ExamMarks.student_id,
#                                         ExamMarks.mark == 4))
# # print(s1.all()[0].)
# print(str(s1.statement.compile(dialect=postgresql.dialect())))
#
# s2 = session.query(Student).filter(Student.name.like('%М%'))
# print(str(s2.statement.compile(dialect=postgresql.dialect())))

# Написать запрос, выводящий фамилии студентов, которые имею стипендию больше, чем у
# студентов вузов Москвы.

s2 = session.query(Student).filter(and_(Student.student_id == University.univ_id,
                                        University.city != 'Москва'))

print(str(s2.statement.compile(dialect=postgresql.dialect())))