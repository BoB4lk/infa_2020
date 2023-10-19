

class Book:

    def __init__(self, book_title, author_name, publisher_name):
        self.__book_title = book_title
        self.__author_name = author_name
        self.__publisher_name = publisher_name

    def set_book_title(self,book_title):
        self.__book_title = book_title

    def set_author_name(self, author_name):
        self.__author_name = author_name

    def set_publisher_name(self, publisher_name):
        self.__publisher_name = publisher_name

    def get_book_title(self):
        return self.__book_title

    def get_author_name(self):
        return self.__author_name

    def get_publisher_name(self):
        return self.__publisher_name

    def __str__(self):
        return (f'название: {self.__book_title}/n'
                f'автор: {self.__author_name}/n'
                f'издатель: {self.__publisher_name}')




