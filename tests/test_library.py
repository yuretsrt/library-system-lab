import unittest
from unittest.mock import Mock
from library import Library
from book import Book
from interfaces import Observer


class TestLibraryArchitecturalPatterns(unittest.TestCase):
    def setUp(self):
        Library._instance = None  # Скидання синглтона перед тестом
        self.library = Library()

    def tearDown(self):
        Library._instance = None  # Очищення після тесту

    def test_singleton_identity(self):
        another_library = Library()
        self.assertIs(self.library, another_library)

    def test_observer_notification_on_add_book(self):
        mock_observer = Mock(spec=Observer)
        self.library.attach(mock_observer)

        book = Book("TDD", "Кент Бек", 2002, book_id=7)
        self.library.add_book(book)

        mock_observer.update.assert_called_once_with("Нова книга в каталозі: TDD")
