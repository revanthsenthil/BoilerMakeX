import os
import psycopg2

conn = psycopg2.connect(os.environ["DATABASE_URL"])

with conn.cursor() as cur:
    
    cur.execute("CREATE DATABASE IF NOT EXISTS courses")
    cur.execute("USE courses")
    cur.execute("CREATE TABLE IF NOT EXISTS courselist (studentID int PRIMARY KEY, name varchar(255), courseList varchar(255))")
    cur.execute("CREATE TABLE IF NOT EXISTS coursetimes(courseID int PRIMARY KEY, course varchar(255), time varchar(255))")
    name = "Harshini"
    course = "CS 25200"
    ID = "0033566852"
    cur.execute(f"INSERT INTO courselist (studentID, name, courseList) VALUES ({ID}, '{name}', '{course}')")
    cur.execute("SELECT * from courselist")
    res1 = cur.fetchall()

    cur.execute("SELECT * from coursetimes")
    res2 = cur.fetchall()

    conn.commit()
    print(res1)
    print(res2)