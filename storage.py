import json
import logging
from book import Book
from user import User
from check import Checkout

# Class for managing storage operations (loading and saving data)
class StorageManager:
    def __init__(self, file_path):
        """
        Initialize a new StorageManager object to handle data persistence.

        Args:
            file_path (str): The file path where data will be stored.
        """
        self.file_path = file_path

    def load_data(self):
        """
        Load data from the specified file path.

        Returns:
            list: A list of dictionaries representing the stored data.

        Raises:
            Exception: If an error occurs while loading the data.
        """
        try:
            with open(self.file_path, 'r') as file:
                logging.info("Reading Existing File")
                data = file.read().strip()
                if not data:
                    logging.warning(f"File {self.file_path} is empty. Returning empty list.")
                    return []
                return json.loads(data)  # Parse JSON data
        except FileNotFoundError:
            logging.warning(f"File not found: {self.file_path}. Returning empty list.")
            return []
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading data from {self.file_path}: {e}")
            raise

    def save_data(self, data, key_field):
        """
        Save data to the specified file path, avoiding duplicates.

        Args:
            data (list): A list of dictionaries representing the data to save.
            key_field (str): The field used as a unique identifier for merging data.

        Raises:
            IOError: If an error occurs while saving the data.
        """
        try:
            # Load existing data
            existing_data = self.load_data()
            
            # Convert existing data to a dictionary for fast lookup
            existing_data_dict = {item[key_field]: item for item in existing_data}

            # Update with new data, avoiding duplicates
            for item in data:
                existing_data_dict[item[key_field]] = item  # Update existing or add new entry

            # Convert back to a list
            merged_data = list(existing_data_dict.values())

            # Write merged data back to the file
            with open(self.file_path, 'w') as file:
                json.dump(merged_data, file)
        except IOError as e:
            logging.error(f"Error saving data to {self.file_path}: {e}")
            raise
    
    def load_books(self):
        """
        Load all books from the storage file.

        Returns:
            list: A list of Book objects.

        Raises:
            Exception: If an error occurs while loading the books.
        """
        try:
            data = self.load_data()
            return [Book(**book) for book in data]
        except Exception as e:
            logging.error(f"Error loading books: {e}")
            raise

    def save_books(self, books):
        """
        Save all books to the storage file.

        Args:
            books (list): A list of Book objects to save.

        Raises:
            Exception: If an error occurs while saving the books.
        """
        try:
            # Convert Book objects to dictionaries and save
            book_data = [book.__dict__ for book in books]
            self.save_data(book_data, 'isbn')
        except Exception as e:
            logging.error(f"Error saving books: {e}")
            raise

    def load_users(self):
        """
        Load all users from the storage file.

        Returns:
            list: A list of User objects.

        Raises:
            Exception: If an error occurs while loading the users.
        """
        try:
            data = self.load_data()
            return [User(**user) for user in data]
        except Exception as e:
            logging.error(f"Error loading users: {e}")
            raise

    def save_users(self, users):
        """
        Save all users to the storage file.

        Args:
            users (list): A list of User objects to save.

        Raises:
            Exception: If an error occurs while saving the users.
        """
        try:
            user_data = [user.__dict__ for user in users]
            self.save_data(user_data, 'user_id')
        except Exception as e:
            logging.error(f"Error saving users: {e}")
            raise

    def load_checkouts(self):
        """
        Load all checkout transactions from the storage file.

        Returns:
            list: A list of Checkout objects.

        Raises:
            Exception: If an error occurs while loading the checkouts.
        """
        try:
            data = self.load_data()
            return [Checkout(**checkout) for checkout in data]
        except Exception as e:
            logging.error(f"Error loading checkouts: {e}")
            raise
    
    def save_checkouts(self, checkouts):
        """
        Save all checkout transactions to the storage file.

        Args:
            checkouts (list): A list of Checkout objects to save.

        Raises:
            Exception: If an error occurs while saving the checkouts.
        """
        try:
            checkout_data = [checkout.__dict__ for checkout in checkouts]
            self.save_data(checkout_data, 'isbn')
        except Exception as e:
            logging.error(f"Error saving checkouts: {e}")
            raise
