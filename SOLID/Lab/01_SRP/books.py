class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author

        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
        return next((b for b in self.books if b.title == title), None)