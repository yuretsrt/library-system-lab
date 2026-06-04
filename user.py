from interfaces import Observer, Notifier
from book import Book

class User:
    def __init__(self, name: str, user_id: int, max_books: int = 2, notifier: Notifier = None):
        self.name = name
        self.user_id = user_id
        self.max_books = max_books
        self.notifier = notifier
        self.borrowed_books = []

    def borrow_book(self, book: Book) -> bool:
        if len(self.borrowed_books) >= self.max_books or book.is_borrowed:
            return False
        if book.borrow():
            self.borrowed_books.append(book)
            if self.notifier:
                self.notifier.notify(f"{self.name} взяв(ла) книгу: {book.title}")
            return True
        return False

    def return_book(self, book: Book) -> bool:
        if book not in self.borrowed_books:
            return False
        if book.return_book():
            self.borrowed_books.remove(book)
            if self.notifier:
                self.notifier.notify(f"{self.name} повернув(ла) книгу: {book.title}")
            return True
        return False

class Reader(User, Observer):
    def update(self, message: str):
        print(f"[Читач {self.name}] отримав сповіщення: {message}")