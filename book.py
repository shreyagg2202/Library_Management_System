# Global list to store books
# books = []

# def add_book(title, author, isbn):
#     books.append({"title": title, "author": author, "isbn": isbn})

# def list_books():
#     for book in books:
#         print(book)

import logging

# Class representing a book in the library
class Book:
    def __init__(self, title, author, isbn, available=True):
        """
        Initialize a new Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (int): The ISBN number of the book (should be unique).
            available (bool): Availability status of the book. Default is True.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available  # Indicates if the book is currently available for checkout
    
    def __str__(self):
        """
        String representation of the Book object, including its availability status.

        Returns:
            str: A string describing the book and its status.
        """
        status = "Available" if self.available else "Checked Out"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"
    
# Class for managing a collection of books
class BookManager:
    def __init__(self):
        """
        Initialize a new BookManager object to manage book collections.
        """
        self.books = []  # List to store all Book objects
    
    def add_book(self, title, author, isbn):
        """
        Add a new book to the collection.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (int): The ISBN number of the book.

        Raises:
            ValueError: If the ISBN is not an integer or if a book with the same ISBN already exists.
        """
        try:
            # Ensure ISBN is an integer
            if not isinstance(isbn, int):
                raise ValueError("ISBN must be an integer.")
            
            # Check for duplicate ISBNs
            if any(book.isbn == isbn for book in self.books):
                print(f"A book with ISBN {isbn} already exists.")
                return

            # Add new book to collection
            new_book = Book(title, author, isbn)
            self.books.append(new_book)
            logging.info(f"Book added: {new_book}")
        except ValueError as ve:
            logging.error(f"Value error when adding book: {ve}")
            raise  
        except Exception as e:
            logging.error(f"Error adding book with Title: {title}, Author: {author}, isbn: {isbn} : {e}")
            raise  
    
    def list_books(self):
        """
        List all books in the collection. If no books are available, notify the user.

        Raises:
            Exception: If an error occurs while listing the books.
        """
        try:
            if not self.books:
                print("No books available in the library.")
            else:
                for book in self.books:
                    print(book)
        except Exception as e:
            logging.error(f"Error listing books: {e}")
            raise

    def find_books_by_isbn(self, isbn):
        """
        Find a book in the collection by its ISBN.

        Args:
            isbn (int): The ISBN number of the book to find.

        Returns:
            Book: The book object if found, None otherwise.

        Raises:
            ValueError: If the ISBN is not an integer.
        """
        try:
            if not isinstance(isbn, int):
                raise ValueError("ISBN must be an integer.")
            
            # Search for book by ISBN
            for book in self.books:
                if book.isbn == isbn:
                    logging.info(f"Book found by ISBN: {book}")
                    return book
            
            logging.warning(f"Book not found by ISBN: {isbn}")
            return None
        except ValueError as ve:
            logging.error(f"Value error when finding book: {ve}")
            raise  
        except Exception as e:
            logging.error(f"Error searching books by ISBN: {isbn} : {e}")
            raise
    
    def find_books_by_title(self, title):
        """
        Find books in the collection by title.

        Args:
            title (str): The title of the book to search for.

        Returns:
            list: A list of books that match the search title.
        """
        try:
            results =  [book for book in self.books if title.lower() in book.title.lower()]
            logging.info(f"Found {len(results)} books with title as: '{title}'")
            return results
        except Exception as e:
            logging.error(f"Error searching books by title: {title} : {e}")
            raise
    
    def find_books_by_author(self, author):
        """
        Find books in the collection by author.

        Args:
            author (str): The author of the book to search for.

        Returns:
            list: A list of books that match the search author.
        """
        try:
            results = [book for book in self.books if author.lower() in book.author.lower()]
            logging.info(f"Found {len(results)} books with author as: '{author}'")
            return results
        except Exception as e:
            logging.error(f"Error searching books by author: {author} : {e}")
            raise

    def remove_book(self, isbn):
        """
        Remove a book from the collection by its ISBN.

        Args:
            isbn (int): The ISBN number of the book to remove.

        Returns:
            bool: True if the book was removed, False otherwise.

        Raises:
            ValueError: If the ISBN is not an integer.
        """
        try:
            if not isinstance(isbn, int):
                raise ValueError("ISBN must be an integer.")
            
            # Find book to remove
            book_to_remove = self.find_books_by_isbn(isbn)
            if book_to_remove:
                self.books.remove(book_to_remove)
                logging.info(f"Book removed: {book_to_remove}")
                return True

            logging.warning(f"Failed to remove book: ISBN {isbn} not found")
            return False
        except ValueError as ve:
            logging.error(f"Value error when removing book: {ve}")
            raise 
        except Exception as e:
            logging.error(f"Error removing book by ISBN: {isbn} : {e}")
            raise
    
    def update_books(self, isbn, title=None, author=None):
        """
        Update a book's information in the collection.

        Args:
            isbn (int): The ISBN number of the book to update.
            title (str, optional): The new title of the book. Defaults to None.
            author (str, optional): The new author of the book. Defaults to None.

        Returns:
            bool: True if the book was updated, False otherwise.

        Raises:
            ValueError: If the ISBN is not an integer.
        """
        try:
            if not isinstance(isbn, int):
                raise ValueError("ISBN must be an integer.")
            
            # Find book to update
            book_to_update = self.find_books_by_isbn(isbn)
            if book_to_update:
                if title:
                    book_to_update.title = title
                if author:
                    book_to_update.author = author
                logging.info(f"Book updated: {book_to_update}")
                return True
            
            logging.warning(f"Failed to update book: ISBN {isbn} not found")
            return False
        except ValueError as ve:
            logging.error(f"Value error when updating book: {ve}")
            raise 
        except Exception as e:
            logging.error(f"Error updating book by ISBN: {isbn} : {e}")
            raise

    def update_book_availability(self, isbn, available):
        """
        Update the availability status of a book in the collection.

        Args:
            isbn (int): The ISBN number of the book to update.
            available (bool): The new availability status of the book.

        Returns:
            bool: True if the book's availability was updated, False otherwise.
        """
        for book in self.books:
            if book.isbn == isbn:
                book.available = available
                return True
        return False
