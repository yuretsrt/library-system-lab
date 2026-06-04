import threading
from interfaces import Subject, Observer
from book import Book

class Library(Subject):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance.books = []
                    cls._instance.observers = []
        return cls._instance

    def attach(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, message: str):
        for obs in self.observers:
            obs.update(message)

    def add_book(self, book: Book):
        self.books.append(book)
        self.notify(f"Нова книга в каталозі: {book.title}")