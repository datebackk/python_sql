import psycopg2

conn = psycopg2.connect(host='127.0.0.1', user='postgres', password='root', dbname='python_sql')

cursor = conn.cursor()

# 1
cursor.execute("SELECT UPPER(surname) ||';'|| UPPER(name) ||';'|| stipend ||';'|| kurs ||';'|| UPPER(city) ||';'|| "
               "birthday ||';'|| univ_id FROM student")

print('1\n', cursor.fetchall())

# 2
cursor.execute("SELECT SUBSTR(NAME, 1, 1) || '.' || SURNAME ||' Место жительства-'|| CITY || '; родился-' || MONTH(birthday) FROM STUDENT LIMIT 1")
print('2\n', cursor.fetchall())


conn.close()
