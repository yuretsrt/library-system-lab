class Book:
    def __init__(self, title: str, author: str, year: int, book_id: int = 0):
        # Валідація даних (Завдання 6)
        if not title or not author or year < 0:
            raise ValueError("Некоректні дані книги")
        self.title = title
        self.author = author
        self.year = year
        self.book_id = book_id
        self.is_borrowed = False

    def borrow(self) -> bool:
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def return_book(self) -> bool:
        if not self.is_borrowed:
            return False
        self.is_borrowed = False
        return True

    def get_info(self):
        return f"{self.title} by {self.author}"

    def get_description(self):
        return f"Book: {self.title}"