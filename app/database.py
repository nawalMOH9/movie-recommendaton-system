import sqlite3

def create_database():
    conn = sqlite3.connect('my_database.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )''')

    conn.commit()
    conn.close()

try:
    create_database()
except:
    True



def add_elemet( email,password):
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users ( username, password) VALUES ( ?, ?)", ( email, password))
    conn.commit()
    conn.close()


def view_all():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    
    conn.close()
    return rows


def check_exist(email,password):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    select_query = "SELECT * FROM users WHERE username = ? and password = ?"
    cursor.execute(select_query, (email,password))
    if cursor.fetchone() is not None:
        return True
    else:
        False
    conn.close()
    
    
    
def return_all():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Query data from the database
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    # Close the database connection
    conn.close()
    
    return data




