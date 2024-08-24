# This is a deliberately poorly implemented main script for a Library Management System.

# import book_management
# import user_management
# import checkout_management

# def main_menu():
#     print("\nLibrary Management System")
#     print("1. Add Book")
#     print("2. List Books")
#     print("3. Add User")
#     print("4. Checkout Book")
#     print("5. Exit")
#     choice = input("Enter choice: ")
#     return choice

# def main():
#     while True:
#         choice = main_menu()
#         if choice == '1':
#             title = input("Enter title: ")
#             author = input("Enter author: ")
#             isbn = input("Enter ISBN: ")
#             book_management.add_book(title, author, isbn)
#             print("Book added.")
#         elif choice == '2':
#             book_management.list_books()
#         elif choice == '3':
#             name = input("Enter user name: ")
#             user_id = input("Enter user ID: ")
#             user_management.add_user(name, user_id)
#             print("User added.")
#         elif choice == '4':
#             user_id = input("Enter user ID: ")
#             isbn = input("Enter ISBN of the book to checkout: ")
#             checkout_management.checkout_book(user_id, isbn)
#             print("Book checked out.")
#         elif choice == '5':
#             print("Exiting.")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()

from book import BookManager
from user import UserManager
from check import CheckoutManager
from storage import StorageManager

import logging

# Set up logging configuration
logging.basicConfig(
    filename='library_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def main():
    """
    Main function to run the Library Management System CLI.
    Handles initialization, user inputs, and program execution.
    """
    try:
        # File paths for storage
        book_file = 'books.json'  # File to store book data
        user_file = 'user.json'  # File to store user data
        checkout_file = 'checkouts.json'  # File to store checkout data

        # Initializing the storage managers for books, users, and checkouts
        book_storage = StorageManager(book_file)
        user_storage = StorageManager(user_file)
        checkout_storage = StorageManager(checkout_file)

        # Load the data from the files
        books = book_storage.load_books()
        users = user_storage.load_users()
        checkouts = checkout_storage.load_checkouts()

        # Initialize the data managers with loaded data
        book_manager = BookManager()
        user_manager = UserManager()
        checkout_manager = CheckoutManager(user_manager, book_manager)

        # Populate managers with the data
        book_manager.books = books
        user_manager.users = users
        checkout_manager.checkouts = checkouts

        # CLI Menu loop
        while True:
            print("\nLibrary Management System")
            print("1: Add a Book")
            print("2: List Books")
            print("3: Search Books")
            print("4: Update a Book")
            print("5: Remove a Book")
            print("6: Add a User")
            print("7: List Users")
            print("8: Search Users")
            print("9: Update a User")
            print("10: Remove a User")
            print("11: Checkout a Book")
            print("12: Return a Book")
            print("13: List Checkouts")
            print("14: Save and Exit")
            print("15: Exit without Saving")
            
            choice = input("Enter your choice: ")

            if choice == '1':
                # Add a new book to the library
                try:
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    isbn = int(input("Enter book ISBN (integer): "))
                    book_manager.add_book(title, author, isbn)
                except ValueError:
                    print("Invalid input. ISBN must be an integer. Please try again.")

            elif choice == '2':
                # List all books in the library
                print("Books in library:")
                book_manager.list_books()

            elif choice == '3':
                # Search for books by title, author, or ISBN
                search_choice = input("Search by (1) Title, (2) Author, (3) ISBN: ")
                if search_choice == '1':
                    title = input("Enter title to search: ")
                    books = book_manager.find_books_by_title(title)
                    for book in books:
                        print(book)
                elif search_choice == '2':
                    author = input("Enter author to search: ")
                    books = book_manager.find_books_by_author(author)
                    for book in books:
                        print(book)
                elif search_choice == '3':
                    try:
                        isbn = int(input("Enter ISBN to search: "))
                        book = book_manager.find_books_by_isbn(isbn)
                        if book:
                            print(book)
                        else:
                            print("Book not found.")
                    except ValueError:
                        print("Invalid input. ISBN must be an integer. Please try again.")

            elif choice == '4':
                # Update book information by ISBN
                try:
                    isbn = int(input("Enter ISBN of the book to update: "))
                    title = input("Enter new title (leave blank to keep current): ")
                    author = input("Enter new author (leave blank to keep current): ")
                    if book_manager.update_books(isbn, title, author):
                        print("Book updated successfully.")
                    else:
                        print("Book not found.")
                except ValueError:
                    print("Invalid input. ISBN must be an integer. Please try again.")

            elif choice == '5':
                # Remove a book from library
                try:
                    isbn = int(input("Enter book ISBN (integer): "))
                    book_manager.remove_book(isbn)
                    print("Book Succesfully removed")
                except ValueError:
                    print("Invalid input. ISBN must be an integer. Please try again.")
            
            elif choice == '6':
                # Add a new user to the library
                try:
                    name = input("Enter user name: ")
                    user_id = int(input("Enter user ID (integer): "))
                    user_manager.add_user(name, user_id)
                except ValueError:
                    print("Invalid input. User ID must be an integer. Please try again.")

            elif choice == '7':
                # List all users in the library
                print("Users in library:")
                user_manager.list_users()

            elif choice == '8':
                # Search for users by name or user ID
                search_choice = input("Search by (1) Name, (2) User ID: ")
                if search_choice == '1':
                    name = input("Enter name to search: ")
                    users = user_manager.find_users_by_name(name)
                    for user in users:
                        print(user)
                elif search_choice == '2':
                    try:
                        user_id = int(input("Enter user ID to search: "))
                        user = user_manager.find_user_by_id(user_id)
                        if user:
                            print(user)
                        else:
                            print("User not found.")
                    except ValueError:
                        print("Invalid input. User ID must be an integer. Please try again.")

            elif choice == '9':
                # Update user information by user ID
                try:
                    user_id = int(input("Enter User ID to update: "))
                    name = input("Enter new name (leave blank to keep current): ")
                    if user_manager.update_user(user_id, name):
                        print("User updated successfully.")
                    else:
                        print("User not found.")
                except ValueError:
                    print("Invalid input. User ID must be an integer. Please try again.")

            elif choice == '10':
                # Remove a user from the library
                try:
                    user_id = int(input("Enter user ID (integer): "))
                    user_manager.remove_user(user_id)
                    print("User Removed Successfully")
                except ValueError:
                    print("Invalid input. User ID must be an integer. Please try again.")
            
            elif choice == '11':
                # Checkout a book to a user
                try:
                    user_id = int(input("Enter user ID: "))
                    isbn = int(input("Enter book ISBN: "))
                    checkout_manager.checkout_book(user_id, isbn)
                except ValueError:
                    print("Invalid input. Values must be integers. Please try again.")

            elif choice == '12':
                # Return a book
                try:
                    user_id = int(input("Enter user ID: "))
                    isbn = int(input("Enter book ISBN to return: "))
                    checkout_manager.return_book(isbn, user_id)
                except ValueError:
                    print("Invalid input. ISBN must be an integer. Please try again.")

            elif choice == '13':
                # List all active checkouts
                print("Checkout list:")
                checkout_manager.list_checkouts()

            elif choice == '14':
                # Save all data and exit the program
                print("Saving data and exiting...")
                try:
                    book_storage.save_books(book_manager.books)
                    user_storage.save_users(user_manager.users)
                    checkout_storage.save_checkouts(checkout_manager.checkouts)
                    print("Data saved successfully.")
                except Exception as save_error:
                    logging.error(f"Error saving data: {save_error}")
                    print("An error occurred while saving the data. Please check the logs.")
                break  # Exit the loop after saving

            elif choice == '15':
                # Exit the program without saving
                print("Exiting without saving.")
                break  # Exit the loop without saving

            else:
                # Invalid choice handling
                print("Invalid choice, please try again.")

    except Exception as e:
        logging.critical(f"Critical error in main application: {e}")
        print("A critical error occurred. Please check the log file for details.")

    finally:
        # Message to indicate session end
        print("Session ended.")

if __name__ == "__main__":
    main()
