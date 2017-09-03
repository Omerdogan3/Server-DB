import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, serverip text, owner text , username text, password text)")
    conn.commit()
    conn.close()


def insert(serverip,owner,username,password):
    if (serverip and owner and username and password) is not "":
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(serverip,owner,username,password))
        conn.commit()
        conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(serverip="",owner=""): #if use pass only one variable it will still works.
    conn = sqlite3.connect("books.db")          #because we started with empty string as parameters.
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE serverip=? OR owner=?",(serverip,owner))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")  # because we started with empty string as parameters.
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,serverip,owner):
    conn = sqlite3.connect("books.db")  # because we started with empty string as parameters.
    cur = conn.cursor()
    cur.execute("UPDATE book SET serverip=?, owner=?",(id,serverip,owner))
    conn.commit()
    conn.close()


connect()
#delete(7)
#update(8,"Moon","John Smooth",1294,123123123)
#print(search(author="John Smooth"))

