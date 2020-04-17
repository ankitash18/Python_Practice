"""

perfomr storign n retrieving a book  from the list
or format of csv file
name,author,reAD\n
"""

books =[]

def create_book_table():
    with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\books.csv','w') :
        pass #just ot make sure fil is there

def add_book(name,author):
    with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\books.csv','a') as file:
             file.write(f'{name},{author},0\n')
    #books.append({'name':name,'author':author,'read':False})

def get_all_books():
    with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\books.csv', 'r') as file:
        lines = [line.strip().split(',') for line  in file.readlines()] #[[],[],[]]
        return [
            {'name':line[0],'author':line[1],'read':line[2]}
            for line in lines
        ]

    #return books


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
       if book['name'] == name:
           book['read'] = '1'
    _save_all_books(books) #oz of naming convetion,it shoyld be private

def _save_all_books(books):
    with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\books.csv', 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")



def delete_book(name):
    books = get_all_books()
    books =[book for book in books if book['name']!= name] #ad eah book to new list if book name is not equat to name argument
    _save_all_books(books)