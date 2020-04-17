from src.resurces import databse_book

USER_CHOICe = """
Enter:
a - > add book
'l' -> to lsit all books
'r'-> to mark the status as read
'd' -> to delete a book
'q -> quit
YOUR CHOICE: """

def menu():
    databse_book.create_book_table()
    user_input = input(USER_CHOICe)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_book()
        elif user_input =='r':
            prompt_read_book()
        elif user_input =='d':
            prompt_delete_book()
        else:
            print("unknow command,try again")
        user_input = input(USER_CHOICe)


def prompt_add_book():
    name = input('Enter the new book name')
    author = input('Enter the author name')
    databse_book.add_book(name,author)

def list_book():
    books = databse_book.get_all_books()
    for book in books:
        read = 'YES' if book['read'] =='1' else 'NO'
        print(f"{book['name']} by {book['author']},read:{read}")


def prompt_read_book():
    name = input('Entee the name of books we just finished')
    databse_book.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of th book you want ot delete')
    databse_book.delete_book(name)


menu()

