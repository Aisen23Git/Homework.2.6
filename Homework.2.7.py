import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except Error as e:
        print(e)
    return connection
#

def create_table(connection, sql):
    try:
        connection.execute(sql)
    except Error as e:
        print(e)
#

def create_products(connection, product):
    try:
        sql = '''
        INSERT INTO products(product_name, product_price,product_quantity)
         VALUES (?, ?, ?)
         '''
        connection.execute(sql,product)
        connection.commit()
    except Error as e:
        print(e)
#
def change_quantity(connection, product):
    try:
        sql = '''
        UPDATE products SET quantity = ? WHERE id = ?
        '''
        connection.execute(sql, product)
        connection.commit()
    except Error as e:
        print(e)
#
def change_price(connection, product):
    try:
        sql = '''
        UPDATE products SET price = ? WHERE id = ?
        '''
        connection.execute(sql, product)
        connection.commit()
    except Error as e:
        print(e)
#
def delete_product(connection,product):
    try:
        sql = '''
        DELETE FROM products WHERE id = ?
        '''
        connection.execute(sql,product)
        connection.commit()
    except Error as e:
        print(e)
#
def select_all_products(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM products''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
#
def select_products(connection,product):
    try:
        sql = '''
        SELECT * FROM products WHERE price < ? and quantity > ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql,product)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
#
def search_product_by_product_name(connection,product_name):
    try:
        sql = '''
        SELECT product_name FROM products WHERE product_name LIKE ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql,("%" + product_name + "%"))
        rows = cursor.fetchall()
        name = []
        for row in rows:
            name.append(row)
        print(name)
    except Error as e:
        print(e)
#
def add_products(connection):
    create_products(connection,('Stickers',30,200))
    create_products(connection,('Ice Cream "Rojok" ',50,35))
    create_products(connection,('Soaps',75,40))
    create_products(connection,('Pepsi',80,20))

    create_products(connection,('Bread',35,40))
    create_products(connection,('Milk',79,30))
    create_products(connection,('Toys',100,60))
    create_products(connection,('Head Phones',250,36))

    create_products(connection, ('Meat', 600, 40))
    create_products(connection, ('Snacks', 80, 20 ))
    create_products(connection, ('Bottle of water 5l Legenda', 70, 20))
    create_products(connection, ('Chocolate "Snikers" ', 60, 20))

    create_products(connection, ('Bananas 1 kg ', 129.58, 100))
    create_products(connection, ('Orange 1 kg', 286.79, 200))
    create_products(connection, ('Yogurt "Чудо"', 120, 30))
    create_products(connection, ('Desk Lamp ', 250, 10))
#
sql_create_product_table = '''
CREATE TABLE products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name VARCHAR(200) NOT NULL , 
product_price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
product_quantity INTEGER(5) NOT NULL DEFAULT 0
)
'''
#
#
db_name = 'hw.db'
connection = create_connection(db_name)
if connection is not None:
    print('Successfully connected ')
    create_table(connection, sql_create_product_table)
    add_products(connection)
    select_products(connection, (100, 5))
    print('products price < 100, quantity > 5')
    search_product_by_product_name(connection, 'cake')
    print('searched product by name')
    change_quantity(connection, (67, 12))
    print('changed quantity by id')
    change_price(connection, (300, 4))
    print('changed price by id')
    delete_product(connection, (8,))
    print('deleted product')
    print('products after changes')
    select_all_products(connection)
    print('all products')
    connection.close()