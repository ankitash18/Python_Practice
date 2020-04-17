from .Database_connection import DataBaseConnection

"""

perfomr storign n retrieving a book  from the list
or format of csv file
name,author,reAD\n
"""



def create_book_table():
    with DataBaseConnection('data.db') as coonnection:
        cursor = coonnection.cursor()

        cursor.execute('Create table if not exists books(name text primary key,author text,read integer)')
    #coonnection.commit()
    #coonnection.close()


def add_book(name,author):
    with DataBaseConnection('data.db') as coonnection:
        cursor = coonnection.cursor()

        cursor.execute('Insert into books values(?,?,0)',(name,author))


def get_all_books():
    with DataBaseConnection('data.db') as coonnection:
        cursor = coonnection.cursor()

        cursor.execute('SELECT * FROM BOOKS')
        books = [{'name':row[0],'author':row[1],'read':row[2]} for row in  cursor.fetchall()] #gives a list of tuple


    return books


def mark_book_as_read(name):
    with DataBaseConnection('data.db') as coonnection:
        cursor = coonnection.cursor()

        cursor.execute('UPDATE BOOKS SET read =1 where name = ?',(name,))



def delete_book(name):
    with DataBaseConnection('data.db') as coonnection:
        cursor = coonnection.cursor()

        cursor.execute('DELETE FROM BOOKS  where name = ?', (name,))
