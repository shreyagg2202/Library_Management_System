# Library_Management_System


#### **1. Overview**

- **Purpose**: To redesign a poorly designed Library Management System to improve its structure, scalability, and usability.
- **Features**:
    - Manage books (add, update, delete, list, and search by title, author, or ISBN).
    - Manage users (add, update, delete, list, and search by name or user ID).
    - Check out and check-in books.
    - Track book availability.
    - Simple logging of operations.

#### **2. System Architecture**

- **Object-Oriented Design**:
    - **Classes**:
        - `Book`: Represents a book entity.
        - `User`: Represents a user entity.
        - `Checkout`: Represents a checkout transaction.
        - `BookManager`, `UserManager`, `CheckoutManager`: Handle operations related to books, users, and checkouts, respectively.
        - `StorageManager`: Handles file-based storage and retrieval of data.
    - **Relationships and Responsibilities**:
        - `BookManager`, `UserManager`, and `CheckoutManager` use `StorageManager` to persist data.
        - Managers handle their respective functions and provide methods for CRUD operations.
- **Data Flow**:
    - User inputs are processed via the Command Line Interface (CLI).
    - Data is stored and retrieved from JSON files through `StorageManager`.

#### **3. Running the Application**

    - Execute the `main.py` file to start the CLI application.
    - Use the provided menu options to interact with the system.

#### **4. Usage**

- **Command Line Interface (CLI) Commands**:
    - `Add a Book`: Add a new book to the library by providing the title, author, and ISBN.
    - `List Books`: List all books currently in the library.
    - `Search Books`: Search for books by title, author, or ISBN.
    - `Update a Book`: Update the details of an existing book.
    - `Remove a Book`: Remove a book from the library by providing the ISBN.
    - `Add a User`: Add a new user to the library system.
    - `List Users`: List all users currently in the system.
    - `Search Users`: Search for users by name or user ID.
    - `Update a User`: Update the details of an existing user.
    - `Remove a User`: Remove a user by providing user ID.
    - `Checkout a Book`: Checkout a book to a user.
    - `Return a Book`: Return a checked-out book to the library.
    - `List Checkouts`: List all current checkouts.
    - `Save and Exit`: Save all data in current session and exit the application.
    - `Exit without Saving`: Exit the application without saving the current session.

#### **5. Class and Method Descriptions**

- **Book Class**:
    - Attributes: `title`, `author`, `isbn`, `available`.
    - Methods: `__str__()`.
- **User Class**:
    - Attributes: `name`, `user_id`.
    - Methods: `__str__()`.
- **Checkout Class**:
    - Attributes: `user_id`, `isbn`.
    - Methods: `__str__()`.
- **Manager Classes (`BookManager`, `UserManager`, `CheckoutManager`)**:
    - Methods for CRUD operations and searching.
- **StorageManager Class**:
    - Methods for loading and saving data (`load_books`, `save_books`, `load_users`, `save_users`, `load_checkouts`, `save_checkouts`).

#### **6. Error Handling**

- **Input Validation**:
    - All user inputs are validated to ensure correct data types and value ranges.
    - Example: ISBN and user ID must be integers.
- **Exception Management**:
    - The system uses `try...except` blocks to catch and handle exceptions.
    - Common exceptions handled include `ValueError`, `FileNotFoundError`, `IOError`, and `JSONDecodeError`.

#### **7. Design Decisions and Patterns**

- **Modular Design**:
    - The system is divided into multiple modules (`book.py`, `user.py`, `check.py`, `storage.py`, `main.py`) for better organization and maintainability.
- **Scalability and Extendibility**:
    - The architecture allows easy addition of new features.
- **Pythonic Idioms and Features**:
    - Use of list comprehensions for filtering and searching.
    - Use of the `logging` module for logging operations and errors.

#### **8. Testing and Validation**

- **Unit Tests**:
    - Each module is thoroughly tested using unit tests.
- **Integration Tests**:
    - Tests covering the full workflow, from adding users and books to checking out and returning books.
- **Edge Case Tests**:
    - Tests for handling invalid inputs, duplicates, and operations on non-existent records.

#### **9. Test Cases**

- **Unit Test Cases for BookManager**:
	-  **Add Book Test**: A book can be added successfully.
	- **Add Book Duplicate ISBN Test**: A book with a duplicate ISBN is not added.
	- **List Books Test**: All books are listed correctly.
	- **Find Book by ISBN Test**: A book can be found by its ISBN.
	- **Find Books by Title Test**: Books can be found by their title.
	- **Remove Book Test**: Ensure A book can be removed successfully.
	- **Update Book Test**: A book’s details can be updated.
	- **Update Nonexistent Book Test**: Attempting to update a nonexistent book fails.

- **Unit Test Cases for UserManager**:
	1. **Add User Test**: A user can be added successfully.
	2. **Add User Duplicate ID Test**: A user with a duplicate ID is not added.
	3. **List Users Test**: All users are listed correctly.
	4. **Find User by ID Test**: A user can be found by their ID.
	5. **Find Users by Name Test**: Users can be found by their name.
	6. **Remove User Test**: A user can be removed successfully.
	7. **Update User Test**: A user’s details can be updated.
	8. **Update Nonexistent User Test**: Attempting to update a nonexistent user fails.

- **Unit Test Cases for CheckoutManager**:
	1. **Checkout Book Test**: A book can be checked out successfully.
	2. **Checkout Book Not Available Test**: A book that is already checked out cannot be checked out again.
	3. **Return Book Test**: A book can be returned successfully.
	4. **Return Nonexistent Checkout Test**: Attempting to return a book that was never checked out fails.
	5. **List Checkouts Test**: All checkouts are listed correctly.

- **Unit Test Cases for StorageManager**:
	- **Save and Load Books Test**: Books can be saved to and loaded from storage.
	- **Save and Load Users Test**: Users can be saved to and loaded from storage.
	- **Save and Load Checkouts Test**:Checkouts can be saved to and loaded from storage.
	- **Load Empty File Test**: Loading data from an empty file returns an empty list.

- **Integration Test Cases**:
	- **Full Workflow Test**: Test the full workflow of adding books and users, checking out and returning books, and listing all data.
	- **Concurrent Checkout and Return Test**: Test the system’s behavior when checking out and returning books concurrently.

- **Edge Case Test Cases**:
	- **Invalid Input Types Test**: Ensure the system handles invalid input types (e.g., non-integer ISBN or user IDs).
	- **Duplicate Entries Test**: Ensure the system handles attempts to add duplicate books or users correctly.
	- **Nonexistent Records Test**: Ensure the system handles nonexistent records (e.g., updating or removing a nonexistent book or user).
	- **File Read/Write Errors Test**: Simulate file read/write errors and ensure the system handles them.
