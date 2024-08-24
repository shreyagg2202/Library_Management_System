# checkouts = []

# def checkout_book(user_id, isbn):
#     checkouts.append({"user_id": user_id, "isbn": isbn})

import logging

# Class representing a checkout transaction in the library system
class Checkout:
    def __init__(self, user_id, isbn):
        """
        Initialize a new Checkout object.

        Args:
            user_id (int): The ID of the user who is checking out the book.
            isbn (int): The ISBN number of the book being checked out.
        """
        self.user_id = user_id
        self.isbn = isbn

    def __str__(self):
        """
        String representation of the Checkout object.

        Returns:
            str: A string describing the checkout transaction.
        """
        return f"User ID: {self.user_id}, ISBN: {self.isbn}"

# Class for managing checkout transactions
class CheckoutManager:
    def __init__(self, user_manager, book_manager):
        """
        Initialize a new CheckoutManager object to manage checkout transactions.

        Args:
            user_manager (UserManager): The manager responsible for user operations.
            book_manager (BookManager): The manager responsible for book operations.
        """
        self.user_manager = user_manager
        self.book_manager = book_manager
        self.checkouts = []  # List to store all Checkout objects

    def is_book_checked_out(self, isbn):
        """
        Check if a book is currently checked out.

        Args:
            isbn (int): The ISBN number of the book to check.

        Returns:
            bool: True if the book is checked out, False otherwise.
        """
        return any(checkout.isbn == isbn for checkout in self.checkouts)
    
    def checkout_book(self, user_id, isbn):
        """
        Process the checkout of a book to a user.

        Args:
            user_id (int): The ID of the user checking out the book.
            isbn (int): The ISBN number of the book being checked out.

        Returns:
            bool: True if the checkout was successful, False otherwise.

        Raises:
            ValueError: If either user_id or isbn is not an integer.
        """
        try:
            if not isinstance(user_id, int) or not isinstance(isbn, int):
                raise ValueError("Values must be integers.")
            
            # Check if the user exists
            if not any(user.user_id == user_id for user in self.user_manager.users):
                print(f"No user with ID {user_id} found.")
                return False
            
            # Check if the book exists and is available
            book = next((book for book in self.book_manager.books if book.isbn == isbn), None)
            if not book:
                print(f"No book with ISBN {isbn} found.")
                return False
            if not book.available:
                print(f"Book with ISBN {isbn} is already checked out.")
                return False
            
            # Proceed with checkout
            new_checkout = Checkout(user_id, isbn)
            self.checkouts.append(new_checkout)
            self.book_manager.update_book_availability(isbn, available=False)
            print(f"Book with ISBN {isbn} checked out by user {user_id}.")
            return True
        except ValueError as ve:
            logging.error(f"Value error when checking out: {ve}")
            raise 
        except Exception as e:
            logging.error(f"Error during checkout for book with ISBN: {isbn} : {e}")
            raise

    def find_checkout_by_isbn(self, isbn):
        """
        Find a checkout transaction by the book's ISBN.

        Args:
            isbn (int): The ISBN number of the book.

        Returns:
            Checkout: The checkout object if found, None otherwise.
        """
        for checkout in self.checkouts:
            if checkout.isbn == isbn:
                return checkout
        return None

    def return_book(self, isbn, user_id):
        """
        Process the return of a book.

        Args:
            isbn (int): The ISBN number of the book being returned.
            user_id (int): The ID of the user returning the book.

        Returns:
            bool: True if the return was successful, False otherwise.

        Raises:
            ValueError: If the ISBN is not an integer.
        """
        try:
            if not isinstance(isbn, int):
                raise ValueError("ISBN must be an integer.")
            
            # Check if the checkout record exists
            checkout = next((co for co in self.checkouts if co.isbn == isbn and co.user_id == user_id), None)
            checkout_to_remove = self.find_checkout_by_isbn(isbn)
            if checkout_to_remove and checkout:
                self.checkouts.remove(checkout_to_remove)
                self.book_manager.update_book_availability(isbn, available=True)
                print('Book returned successfully')
                logging.info(f"Book returned: {checkout_to_remove}")
                return True
            
            print("Failed to return book. It may not be checked out.")
            logging.warning(f"Failed to return book: ISBN {isbn} not found in checkouts")
            return False
        except ValueError as ve:
            logging.error(f"Value error when returning book: {ve}")
            raise 
        except Exception as e:
            logging.error(f"Error during return of book with ISBN : {isbn} : {e}")
            raise
    
    def list_checkouts(self):
        """
        List all checkout transactions.

        Raises:
            Exception: If an error occurs while listing the checkouts.
        """
        try:
            for checkout in self.checkouts:
                print(checkout)
        except Exception as e:
            logging.error(f"Error listing checkouts: {e}")
            raise
