from library import Library
from book import Book
from user import Reader


def main():
    lib = Library()
    reader = Reader("Олексій", user_id=1)
    lib.attach(reader)

    book = Book("Чиста архітектура", "Роберт Мартін", 2018, book_id=10)
    lib.add_book(book)


if __name__ == "__main__":
    main()
