import os
import pymysql
cnx = pymysql.connect(user='hamadahorizon',
                      passwd='',
                      host=os.getenv('IP','0.0.0.0'),
                      db='bookstore')
            
cur = cnx.cursor()
# cur.execute('CREATE DATABASE bookStore')

'''bookTable = """CREATE TABLE books(
            book_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            author_fname VARCHAR(100),
            author_lname VARCHAR(100),
            released_year INT,
            stock_quantity INT,
            pages INT)"""
bookTable = ("DROP TABLE books")
cur.execute(bookTable)'''

customers = """CREATE TABLE customers(
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            email VARCHAR(100))"""

#cur.execute(customers)

orders = """CREATE TABLE orders(
          id INT AUTO_INCREMENT PRIMARY KEY,
          orders_date DATE,
          amount DECIMAL(8,2),
          customer_id INT,
          FOREIGN KEY(customer_id) REFERENCES customers(id))"""

#cur.execute(orders)
ins_customers = "INSERT INTO customers(first_name, last_name, email)" \
                 "VALUES('Bruce', 'Willis', 'bruce@gmail.com')," \
                     "('George', 'Micheal', 'gm@gmail.com')," \
                     "('David', 'Bowie', 'david@gmail.com')," \
                     "('Blue', 'Steele', 'blue@gmail.com')," \
                     "('Bette', 'Davis', 'bette@aol.com')"
#cur.execute(ins_customers)
ins_orders = "INSERT INTO orders(orders_date, amount, customer_id)" \
              "VALUES('2016/02/10', 99.99, 1)," \
                  "('2017/05/1', 35.50, 1)," \
                  "('2010/12/24', 800.67, 2)," \
                  "('2016/06/01', 12.50, 2)," \
                  "('2018/03/10', 99.99, 5)" 

cur.execute(ins_orders)
# cur.execute(ins_orders)


cnx.commit()

cnx.close()
