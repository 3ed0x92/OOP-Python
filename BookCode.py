#Book Class
import json

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = True
        self.borrower = None

    def borrow(self, borrower):
        if self.is_available:
            self.is_available = False
            self.borrower = borrower
            return True
        return False

    def return_book(self):
        self.is_available = True
        self.borrower = None

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre}) - {'Available' if self.is_available else f'Borrowed by {self.borrower.name}'}"
      
#Member Class

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow(self):
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}) - Borrowed books: {[book.title for book in self.borrowed_books]}"
      
#Librarian Class

class Librarian:
    def __init__(self, name, librarian_id):
        self.name = name
        self.librarian_id = librarian_id

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, book):
        library.remove_book(book)

    def __str__(self):
        return f"Librarian: {self.name} (ID: {self.librarian_id})"


#Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.librarians = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def add_member(self, member):
        self.members.append(member)

    def add_librarian(self, librarian):
        self.librarians.append(librarian)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def save_to_file(self, filename):
        data = {
            "books": [
                {"title": book.title, "author": book.author, "genre": book.genre, "is_available": book.is_available, "borrower": book.borrower.name if book.borrower else None}
                for book in self.books
            ],
            "members": [
                {"name": member.name, "member_id": member.member_id, "borrowed_books": [book.title for book in member.borrowed_books]}
                for member in self.members
            ],
            "librarians": [
                {"name": librarian.name, "librarian_id": librarian.librarian_id}
                for librarian in self.librarians
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        self.books = [Book(**book_data) for book_data in data["books"]]
        self.members = [Member(**member_data) for member_data in data["members"]]
        self.librarians = [Librarian(**librarian_data) for librarian_data in data["librarians"]]

#Main Function

def main():
    library = Library()

    # Create and add books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
    book2 = Book("1984", "George Orwell", "Dystopian")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Create and add members
    member1 = Member("Alice", 1)
    member2 = Member("Bob", 2)
    library.add_member(member1)
    library.add_member(member2)

    # Create and add a librarian
    librarian = Librarian("Mr. Batot", 1)
    library.add_librarian(librarian)

    # Member borrows a book
    print(member1.borrow_book(book1))

    # Member tries to borrow the same book again
    print(member2.borrow_book(book1))

    # Member returns the book
    print(member1.return_book(book1))

    # Save library data to file
    library.save_to_file("library_data.json")

    # Load library data from file
    new_library = Library()
    new_library.load_from_file("library_data.json")

    # Display the books in the new library
    for book in new_library.books:
        print(book)

if __name__ == "__main__":
    main()



