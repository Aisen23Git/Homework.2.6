import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_countries_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL
        )
        '''
    )
    conn.commit()


def insert_countries(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO countries (title) VALUES (?)", ('USA',))
    cursor.execute("INSERT INTO countries (title) VALUES (?)", ('Germany',))
    cursor.execute("INSERT INTO countries (title) VALUES (?)", ('China',))
    cursor.execute("INSERT INTO countries (title) VALUES (?)", ('France',))
    cursor.execute("INSERT INTO countries (title) VALUES (?)", ('Russia',))
    cursor.execute("INSERT INTO countries (title) VALUES (?)", ('Kyrgyzstan',))
    conn.commit()



def create_cities_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities 
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title TEXT NOT NULL,
    area DEFAULT 0, 
    country_id INTERGER,
    FOREIGN KEY(country_id) REFERENCES countries(id))
    ''')
    conn.commit()


def insert_cities(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cities(title, area, country_id)VALUES(?,?,?)", ('Berlin', 120, 2))
    cursor.execute("INSERT INTO cities(title, area, country_id)VALUES(?,?,?)", ('Dresden', 1223, 2 ))
    cursor.execute("INSERT INTO cities(title, area, country_id)VALUES(?,?,?)", ('Paris', 891, 4))
    cursor.execute("INSERT INTO cities(title, area, country_id)VALUES(?,?,?)", ('Boston', 12640, 1))
    cursor.execute("INSERT INTO cities(title, area, country_id)VALUES(?,?,?)", ('Los Angeles', 6340, 1))
    cursor.execute("INSERT INTO cities(title, area, country_id)VALUES(?,?,?)", ('Bishkek', 310, 6))
    cursor.execute("INSERT INTO cities(title, area, country_id)VALUES(?,?,?)", ('Saint-Peterburg', 755, 5))
    cursor.execute("INSERT INTO cities(title, area, country_id)VALUES(?,?,?)", ('Beijing', 173, 3))
    conn.commit()


def create_students_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students 
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    city_id INTEGER, 
    FOREIGN KEY(city_id) REFERENCES cities(id))
    ''')
    conn.commit()


def insert_students(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Asan', 'Uson', 6))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Marcus', 'Dawn', 1))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Douglas', 'Manch', 2))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Haitz', 'Ghriht', 3))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Leny', 'Smonte', 4))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Johny', 'Sorty', 5))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Charles', 'Mangle', 6))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Joe', 'Rein', 7))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('James', 'Clavor', 3))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Weisel', 'Hortsz', 2))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Meneal', 'Zhwirs', 4))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Mongle', 'Shulz', 5))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Oliver', 'Morgan', 1))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Solt', 'Fhridrich', 6))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Manny', 'Cholo', 7))
    cursor.execute("INSERT INTO students(first_name, last_name, city_id) VALUES(?,?,?)", ('Vladimir', 'Zolotov', 5))
    conn.commit()


def get_cities(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM cities")
    cities = cursor.fetchall()
    return cities


def get_students_by_city(conn, city_id):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area " 
        "FROM students "
        "JOIN cities ON students.city_id = cities.id " 
        "JOIN countries ON cities.country_id = countries.id "
        "WHERE cities.id = ?", (city_id,))

    students = cursor.fetchall()
    return students


def print_cities(cities):
    print("List of cities:")
    for city in cities:
        print(city[0])


def print_students(students):
    print("Information about the students in the selected city:")
    for student in students:
        print("Name:", student[0])
        print("Last name:", student[1])
        print("Country:", student[2])
        print("City: ", student[3])
        print("Area of the city", student[4])
        print("_______________________________")


def main():
    conn = create_connection('stude.db')
    if conn is not None:
        print("Connected to Data Base! ")
    create_countries_table(conn)
    insert_countries(conn)

    create_cities_table(conn)
    insert_cities(conn)

    create_students_table(conn)
    insert_students(conn)

    cities = get_cities(conn)

    print_cities(cities)

    while True:
        city_id = int(input("You can display a list of students"
                            "by selected city id from the list of cities below," 
                            "to exit the program, enter 0: "))
        if city_id == 0:
            break
        students = get_students_by_city(conn, city_id)
        print_students(students)
    conn.close()


if __name__ == "__main__":
    main()