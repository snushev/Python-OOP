from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content

class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass

class Formatter:
    def format(self, book: Book) -> str:
        return book.content

class PaperFormat:
    def format(self, book: Book):
        return book.content[:5]

class Printer:
    def get_book(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book