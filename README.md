This code can explain oop in python and difreence betwwn funcation

Explanation Book Code
1- Book Class:

    __init__: Initializes a book with a title, author, genre, availability status, and borrower.
    borrow: Marks the book as borrowed and sets the borrower.
    return_book: Marks the book as available and clears the borrower.
    __str__: Returns a string representation of the book.
    
2- Member Class:

    __init__: Initializes a member with a name, member ID, and a list of borrowed books.
    borrow_book: Borrows a book if it is available.
    return_book: Returns a borrowed book.
    __str__: Returns a string representation of the member.
    
3- Librarian Class:

    __init__: Initializes a librarian with a name and librarian ID.
    add_book: Adds a book to the library.
    remove_book: Removes a book from the library.
    __str__: Returns a string representation of the librarian.
    
4- Library Class:

    __init__: Initializes the library with lists of books, members, and librarians.
    add_book: Adds a book to the library.
    remove_book: Removes a book from the library.
    add_member: Adds a member to the library.
    add_librarian: Adds a librarian to the library.
    find_book_by_title: Finds a book by its title.
    save_to_file: Saves the library data to a JSON file.
    load_from_file: Loads the library data from a JSON file.
    
5- Main Function:

    Demonstrates the functionality of the library by creating books, members, and a librarian, borrowing and returning books, and saving/loading data from a file.
