import os
import pymysql
cnx = pymysql.connect(user='hamadahorizon',
                      passwd='',
                      host=os.getenv('IP','0.0.0.0'),
                      db='classroom')
            
cur = cnx.cursor()


student = """CREATE TABLE students(
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100)
            )"""

#cur.execute(student)

paper = """CREATE TABLE papers(
           title VARCHAR(100),
           grade INT,
           student_id INT,
           FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
           )"""
cur.execute(paper)
n_student = "INSERT INTO students(first_name)" \
             "VALUES('Caleb'),('Samantha'),('Raj'),('Carlos'),('LISA')"



cnx.commit()
cnx.close()

