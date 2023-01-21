import os
import psycopg2

conn = psycopg2.connect(os.environ["DATABASE_URL"])

with conn.cursor() as cur:
    
    cur.execute("CREATE DATABASE IF NOT EXISTS courses")
    cur.execute("USE courses")
    cur.execute("CREATE TABLE IF NOT EXISTS courselist (studentID int PRIMARY KEY, Name varchar(255), CourseList varchar(255))")
    # res = cur.fetchall()
    conn.commit()
    # print(res)