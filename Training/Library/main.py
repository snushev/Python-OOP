
class Book:
    def __init__(self, title: str, author: str, year: int, genre: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value == "":
            raise ValueError("Invalid title")
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if value == "":
            raise ValueError("Invalid author")
        self.__author = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if value == "":
            raise ValueError("Invalid genre")
        self.__genre = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value <= 0:
            raise ValueError("Invalid year")
        self.__year = value

    def __str__(self):
        return f"Book: {self.title} by {self.author} ({self.year}) - Genre: {self.genre}"


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be an empty string!")
        self.__name = value

class Reader(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age
        self.__borrowed_books = []

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Invalid age.")
        self.__age = value

    def borrow_book(self, book: Book):
        if book in self.__borrowed_books:
            return f"Book {book.title} already borrowed"
        self.__borrowed_books.append(book)
        if book not in Librarian.library:
            return f"Book is not currently in the library."
        Librarian.library.remove(book)
        return f"Book {book.title} has been added to your list."

    def return_book(self, book_name: str):
        for current_book in self.__borrowed_books:
            if current_book.title == book_name:
                self.__borrowed_books.remove(current_book)
                Librarian.library.append(current_book)
                return f"{current_book.title} has been returned."

        return f"There is no such book in your list."

    def __str__(self):
        result = ""
        if self.__borrowed_books:
            result += f"This is {self.name}, {self.age} years old, and has the books:"
            for current_book in self.__borrowed_books:
                result += f"\n{current_book}"
            return result
        return f"This is {self.name}, {self.age} years old, and has no books"

class Librarian(Person):
    library = []
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, book: Book):
        if book in self.library:
            return f"{book.title} is already in the library."
        self.library.append(book)
        return f"{book.title} is successfully added to the library."

    def remove_book(self, book_name):
        for current_book in self.library:
            if current_book.title == book_name:
                self.library.remove(current_book)
                return f"{current_book.title} successfully removed from the library."
        return f"No book called {book_name} in the library."

    def __str__(self):
        result = f"Librarian on shift is {self.name}.\n"\
                 f"Current books are:"
        for i in self.library:
            result += f"\n{i}"
        return result


# Създаване на книги
book1 = Book("1984", "George Orwell", 1949, "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")

# Създаване на библиотекар
librarian = Librarian("Alice")

# Добавяне на книги към библиотеката
print(librarian.add_book(book1))  # Output: 1984 is successfully added to the library.
print(librarian.add_book(book2))  # Output: To Kill a Mockingbird is successfully added to the library.

# Създаване на читател
reader = Reader("John", 25)

# Читателят взема книга
print(reader.borrow_book(book1))  # Output: Book 1984 has been added to your list.

# Читателят връща книга
print(reader.return_book("1984"))  # Output: 1984 has been returned.

# Извеждане на информация за библиотекаря
print(librarian)

# Извеждане на информация за читателя
print(reader)

