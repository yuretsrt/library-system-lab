import unittest
from unittest.mock import Mock
from user import User
from book import Book
from interfaces import Notifier

class TestUser(unittest.TestCase):
    def setUp(self):
        self.mock_notifier = Mock(spec=Notifier)
        self.user = User("Олексій", user_id=10, max_books=1, notifier=self.mock_notifier)
        self.book = Book("Чистий код", "Роберт Мартін", 2008, book_id=5)

    def test_borrow_book_notifies_observer(self):
        result = self.user.borrow_book(self.book)
        self.assertTrue(result)
        self.mock_notifier.notify.assert_called_once_with("Олексій взяв(ла) книгу: Чистий код")

    def test_borrow_limit_exceeded(self):
        self.user.borrow_book(self.book)
        another_book = Book("Патерни", "Е. Гамма", 1994, book_id=6)
        result = self.user.borrow_book(another_book)
        self.assertFalse(result)