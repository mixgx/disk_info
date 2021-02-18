import sqlite3

from sqlite3 import Error


""""""
TEST = 0
""""""


def sql_connection():

    try:

        con = sqlite3.connect('disk_info.db')

        return con

    except Error:

        print(Error)

def sql_table(con, update, new, string):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE IF NOT EXISTS disk(id integer PRIMARY KEY, total text, free text, hireDate text)")

    if update:
        cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    if new:
        cursorObj.execute(string)
    else:
        cursorObj.execute('SELECT * FROM disk')
        #print('test')
        rows = cursorObj.fetchall()
        #rows = list(rows[0])
        #print(rows)
        con.close()
        return rows

    con.commit()
    #con.commit()
    
    #rows = cursorObj.fetchall()
    #rows = list(rows[0])

    #print(rows[0])

    """for row in rows:

        print(row)"""

def sql_drop(con):

    cursorObj = con.cursor()

    cursorObj.execute('DROP table if exists disk')

    con.commit()
    
if TEST == 1:
    con = sql_connection()
    test = sql_table(con, False, False, 't')
    print(test)