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

#cur.execute(ins_orders)
# cur.execute(ins_orders)

# 2. JOIN:

# let's say i want to find the orders that have been placed by bruce willis
# -1 where gonna first try to find the customers that ho's make that orders in customers table
statement = 'SELECT * FROM customers WHERE last_name="Willis"'
cur.execute(statement)
# to delete: delete from customers where id>5;

#-2 then i try to find where is the orders in the orders table
statement_2 = 'SELECT * FROM orders WHERE customer_id = 1'
''' SELECT * FROM orders WHERE customer_id = 
        (
            SELECT id FROM customers WHERE last_name="Willis"
        )'''    
cur.execute(statement_2)


# -3 so that was a two step process and we could simplify that and do it all at once
'''i dont want just customer_id i wanted it see the name of who made the order and this lead us to join 
so its take two tables and we can join them by take the data from one and from another and stick them '''

# .1 implicit inner join
# statement_3 = 'SELECT * FROM customers, orders WHERE customers.id = orders.customer_id'
# if we want just the first name last_name order_date and amount
statement_3 = 'SELECT first_name, last_name, orders_date, amount FROM customers, orders' \
               'WHERE customers.id = orders.customer_id'
# so we have joined them together using what's know an an implicit inner join 

# .2 explicit inner join
statement_4 = 'SELECT first_name, last_name, orders_date, amount  FROM customers' \
                'JOIN orders ON customers.id = orders.customer_id'

# -4 Left Join:
# .1 Make it fancier
# we can use GROUP BY and SUM the amount to get the total amount for every customers
statement_5 = 'SELECT first_name, last_name, orders_date, SUM(amount) AS total_spent  FROM customers' \
                'JOIN orders ON customers.id = orders.customer_id' \
                'GROUP BY orders.customer_id ORDER BY total_spent DESC'
                
statement_6 = 'SELECT first_name, last_name, orders_date, amount  FROM customers' \
                'LEFT JOIN orders ON customers.id = orders.customer_id'

statement_7 = 'SELECT first_name, last_name, orders_date, IFNULL(SUM(amount), 0) AS total_spent' \
                'FROM customers LEFT JOIN orders ON customers.id = orders.customer_id '\
                'GROUP BY customers.id ORDER BY total_spent'

'''the key difference with inner join, we have the union , and also the half left part in addition, so 
every customer in our case which can be useful if we wanted tp see thing like which customers hadn't
ordered things'''

# 2. Right Join
cnx.commit()

cnx.close()
