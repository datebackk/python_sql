import psycopg2

conn = psycopg2.connect(host='127.0.0.1', user='postgres', password='root', dbname='python_sql')

cursor = conn.cursor()

# org.PostreSQL.Dialect

# Вариант 1
print('Вариант 1\n')
cursor.execute("SELECT name ||' '|| surname ||' '|| kurs FROM STUDENT WHERE kurs=4 OR kurs=5")
print('1\n', cursor.fetchall())

cursor.execute("SELECT CONCAT(name, ' ', surname, ' ', to_char(birthday, 'YYYY'), ' г.р') FROM STUDENT")
print('2\n', cursor.fetchall())


# Вариант 2
print('\nВариант 2\n')
cursor.execute("SELECT STUDENT.name ||' '|| ROUND(AVG(mark), 2) FROM EXAM_MARKS JOIN STUDENT ON EXAM_MARKS.student_id=STUDENT.student_id  GROUP BY(STUDENT.name)")
print('1\n', cursor.fetchall())

cursor.execute("SELECT CONCAT(name, ' ', surname, ' (', kurs, ' курс)' ) FROM STUDENT")
print('2\n', cursor.fetchall())


