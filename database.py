from bottle import Bottle, request, run, template, static_file, redirect
import sqlite3

# Change this if the database name is changed
database_name = 'userDatabase.db'

"""
This program handles all SQL logic and traffic.
"""


def create_user(user):
    """
    Creates a new user in the database.

    Args:
        user (User): The user object containing the username and password.

    Returns:
        bool: True if the user is created successfully, False if the username already exists.

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute("SELECT Username FROM Users WHERE Username = ?", (user.get_username(),))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        return False
    else:
        # Insert the new user into the 'Users' table
        cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)",
                       (user.get_username(), user.get_password()))
        conn.commit()
        conn.close()
        return True


def check_credentials(username, password):
    """
    Checks the credentials of a user.

    Args:
        username (str): The username.
        password (str): The password.

    Returns:
        bool: True if the credentials are valid, False otherwise.

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query to check the credentials
    cursor.execute('SELECT * FROM Users WHERE Username=? AND Password=?', (username, password))
    result = cursor.fetchone()

    # Close the connection
    conn.close()

    if result is None:
        return False
    else:
        return True


def get_user_data_by_id(user_id):
    """
    Retrieves user data from the database by ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        tuple: User data if successful, None if the user does not exist.

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query to get user data
    cursor.execute('SELECT * FROM Users WHERE ID=?', (user_id,))
    user_data = cursor.fetchone()

    # Close the connection
    conn.close()

    return user_data if user_data else None


def get_user_data_by_username(username):
    """
    Retrieves user data from the database by username.

    Args:
        username (str): The username.

    Returns:
        tuple: User data if successful, None if the user does not exist.

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query to get user data
    cursor.execute('SELECT * FROM Users WHERE Username=?', (username,))
    user_data = cursor.fetchone()

    # Close the connection
    conn.close()

    return user_data if user_data else None


def save_user_draft_by_username(username, title, content):
    """
    Saves a user draft in the database.

    Args:
        username (str): The username.
        title (str): The draft title.
        content (str): The draft content.

    Returns:
        None

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("SELECT Username FROM Users WHERE Username = ?", (username,))
    existing_user = cursor.fetchone()

    # Insert the new draft into the 'Users' table
    cursor.execute("INSERT INTO Users (Title, Draft) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()


def publish_review(username, title, content):
    """
    Publishes a review by adding it to the 'Reviews' table in the database.

    Args:
        username (str): The username.
        title (str): The review title.
        content (str): The review content.

    Returns:
        None

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Reviews (Username, Title, Content) VALUES (?, ?, ?)", (username, title, content))
    conn.commit()
    conn.close()


def get_published_reviews():
    """
    Retrieves all published reviews from the 'Reviews' table in the database.

    Returns:
        list: List of reviews (tuples) if successful.

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query to get all reviews
    cursor.execute('SELECT * FROM Reviews')
    reviews_data = cursor.fetchall()

    # Close the connection
    conn.close()

    return reviews_data


def change_password(username, new_password):
    """
    Processes the change password form and updates the user's password.

    Returns:
        str: Redirects to the members page.

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Update the user's password in the database
    cursor.execute('UPDATE Users SET Password=? WHERE Username=?', (new_password, username))
    conn.commit()
    conn.close()
