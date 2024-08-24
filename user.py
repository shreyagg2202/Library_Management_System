# users = []

# def add_user(name, user_id):
#     users.append({"name": name, "user_id": user_id})

import logging

# Class representing a user in the library system
class User:
    def __init__(self, name, user_id):
        """
        Initialize a new User object.

        Args:
            name (str): The name of the user.
            user_id (int): The unique ID of the user.
        """
        self.name = name
        self.user_id = user_id
    
    def __str__(self):
        """
        String representation of the User object.

        Returns:
            str: A string describing the user.
        """
        return f"Name: {self.name}, User ID: {self.user_id}"
    
# Class for managing a collection of users
class UserManager:
    def __init__(self):
        """
        Initialize a new UserManager object to manage user collections.
        """
        self.users = []  # List to store all User objects

    def add_user(self, name, user_id):
        """
        Add a new user to the collection.

        Args:
            name (str): The name of the user.
            user_id (int): The unique ID of the user.

        Raises:
            ValueError: If the user ID is not an integer or if a user with the same ID already exists.
        """
        try:
            # Ensure user ID is an integer
            if not isinstance(user_id, int):
                raise ValueError("User ID must be an integer.")
            
            # Check for duplicate user IDs
            if any(user.user_id == user_id for user in self.users):
                print(f"A user with ID {user_id} already exists.")
                return
            
            # Add new user to collection
            new_user = User(name, user_id)
            self.users.append(new_user)
            logging.info(f"User added: {new_user}")
        except ValueError as ve:
            logging.error(f"Value error when adding user: {ve}")
            raise
        except Exception as e:
            logging.error(f"Error adding user: {e}")
            raise

    def list_users(self):
        """
        List all users in the collection.

        Raises:
            Exception: If an error occurs while listing the users.
        """
        try:
            for user in self.users:
                print(user)
        except Exception as e:
            logging.error(f"Error listing users: {e}")
            raise

    def find_user_by_id(self, user_id):
        """
        Find a user in the collection by their ID.

        Args:
            user_id (int): The unique ID of the user to find.

        Returns:
            User: The user object if found, None otherwise.

        Raises:
            ValueError: If the user ID is not an integer.
        """
        try:
            if not isinstance(user_id, int):
                raise ValueError("User ID must be an integer.")
            
            # Search for user by ID
            for user in self.users:
                if user.user_id == user_id:
                    logging.info(f"User found by ID: {user}")
                    return user
            
            logging.warning(f"User not found by ID: {user_id}")
            return None
        except ValueError as ve:
            logging.error(f"Value error when searching user: {ve}")
            raise
        except Exception as e:
            logging.error(f"Error searching users by id: {user_id} : {e}")
            raise

    def find_users_by_name(self, name):
        """
        Find users in the collection by name.

        Args:
            name (str): The name of the user to search for.

        Returns:
            list: A list of users that match the search name.
        """
        try:
            results = [user for user in self.users if name.lower() in user.name.lower()]
            logging.info(f"Found {len(results)} users with name as: '{name}'")
            return results
        except Exception as e:
            logging.error(f"Error searching users by name: {name} : {e}")
            raise

    def remove_user(self, user_id):
        """
        Remove a user from the collection by their ID.

        Args:
            user_id (int): The unique ID of the user to remove.

        Returns:
            bool: True if the user was removed, False otherwise.

        Raises:
            ValueError: If the user ID is not an integer.
        """
        try:
            if not isinstance(user_id, int):
                raise ValueError("User ID must be an integer.")
            
            # Find user to remove
            user_to_remove = self.find_user_by_id(user_id)
            if user_to_remove:
                self.users.remove(user_to_remove)
                logging.info(f"User removed: {user_to_remove}")
                return True
            
            logging.warning(f"Failed to remove user: ID {user_id} not found")
            return False
        except ValueError as ve:
            logging.error(f"Value error when removing user: {ve}")
            raise
        except Exception as e:
            logging.error(f"Error removing users by id: {user_id} : {e}")
            raise

    def update_user(self, user_id, name=None):
        """
        Update a user's information in the collection.

        Args:
            user_id (int): The unique ID of the user to update.
            name (str, optional): The new name of the user. Defaults to None.

        Returns:
            bool: True if the user was updated, False otherwise.

        Raises:
            ValueError: If the user ID is not an integer.
        """
        try:
            if not isinstance(user_id, int):
                raise ValueError("User ID must be an integer.")
            
            # Find user to update
            user_to_update = self.find_user_by_id(user_id)
            if user_to_update:
                if name:
                    user_to_update.name = name
                    logging.info(f"User updated: {user_to_update}")
                return True
            
            logging.warning(f"Failed to update user: ID {user_id} not found")
            return False   
        except ValueError as ve:
            logging.error(f"Value error when updating user: {ve}")
            raise 
        except Exception as e:
            logging.error(f"Error updating user by id: {user_id} : {e}")
            raise
