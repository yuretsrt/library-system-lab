import unittest
from parameterized import parameterized
from book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("1984", "Джордж Орвелл", 1949, book_id=1)

    def test_initial_state(self):
        self.assertFalse(self.book.is_borrowed)

    def test_borrow_success(self):
        res = self.book.borrow()
        self.assertTrue(res)
        self.assertTrue(self.book.is_borrowed)

    def test_borrow_already_borrowed(self):
        self.book.borrow()
        res = self.book.borrow()
        self.assertFalse(res)

    def test_return_book_not_borrowed(self):
        res = self.book.return_book()
        self.assertFalse(res)

class TestBookValidation(unittest.TestCase):
    @parameterized.expand([
        ("", "Автор", 2020, ValueError),
        ("Назва", "", 2020, ValueError),
        ("Назва", "Автор", -10, ValueError),
    ])
    def test_invalid_book_creation(self, title, author, year, expected_exception):
        with self.assertRaises(expected_exception):
            Book(title, author, year)