# 50 Н а п ишите з а п рос, который в ып олняет в ыв од сп иска унив ерситетов с
# рейтингом, п рев ышающ им 300, в месте со з на ч ением максимального
# р а змера стип енд ии, п олуч аемой студ ентами в этих унив ерситетах.

select university.univ_name, university.rating, MAX(student.stipend)
from university join student on university.univ_id = student.univ_id
and university.rating > 300 group by university.univ_name, student.student_id, university.rating





# 47 Н а п ишите з а п рос, который в ып олняет в ыв од д анных о фамилиях
# студ ентов , сд а в а вш и х экз амены, в месте с наименов а ниями кажд ого
# сд анного ими п редмета обуч ения.

select stud.surname, sub.subj_name from student stud
    join exam_marks em on stud.student_id = em.student_id and em.mark > 2
    join subject sub on sub.subj_id = em.subj_id


# 51 Н а п ишите з а п р ос на в ыд а ч у сп иска фамилий студ ентов (в а лфа в итном
# п оряд ке) в месте со з на ч ением рейтинга унив ерситета , где кажд ый из них
# уч ится, в ключ ив в сп исок и тех студ ентов , д ля которых в ба зе д анных не
# ука з ано место их уч ебы.

select student.surname, u.rating from student join university u
    on student.univ_id = u.univ_id
union select student.surname, u2.rating from student join university u2 on student.univ_id is null