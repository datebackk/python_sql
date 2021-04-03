import psycopg2

conn = psycopg2.connect(host='127.0.0.1', user='postgres', password='root', dbname='python_sql')

cursor = conn.cursor()

cursor.execute("SELECT name, ROUND(stipend * 1.2, 2) FROM STUDENT ORDER BY stipend")
print('21 a)\n', cursor.fetchall())