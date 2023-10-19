from bottle import Bottle, request, run, template, static_file, redirect
import sqlite3

# Change this if database name is changed
database_name = 'userDatabase.db'

"""
THIS PROGRAM HANDLES ALL SQL LOGIC AND TRAFFIC
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
    cursor.execute("SELECT Username FROM Users WHERE Username = ?", (user.get_user_name(),))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        return False
    else:
        # Insert the new user into the 'Users' table
        cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", (user.get_user_name(), user.get_password()))
        conn.commit()
        conn.close()
        return True


def check_credentials(user_name, user_password):
    """
    Checks the credentials of a user.

    Args:
        user_name (str): The username.
        user_password (str): The password.

    Returns:
        bool: True if the credentials are valid, False otherwise.

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query to check the credentials
    cursor.execute('SELECT * FROM Users WHERE Username=? AND password=?', (user_name, user_password))
    result = cursor.fetchone()

    # Close the connection
    conn.close()

    if result is None:
        return False
    else:
        return True


def get_user_data_by_id(UserID):
    """
    Retrieves user data from the database by ID.

    Args:
        UserID (int): The ID of the user.

    Returns:
        tuple: User data if successful, None if the user does not exist.

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query to get user data
    cursor.execute('SELECT * FROM Users WHERE ID=?', (UserID,))
    user_data = cursor.fetchone()

    # Close the connection
    conn.close()

    return user_data if user_data else None


def get_user_data_by_username(user_name):
    """
    Retrieves user data from the database by username.

    Args:
        user_name (str): The username.

    Returns:
        tuple: User data if successful, None if the user does not exist.

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query to get user data
    cursor.execute('SELECT * FROM Users WHERE username=?', (user_name,))
    user_data = cursor.fetchone()

    # Close the connection
    conn.close()

    return user_data if user_data else None


def save_user_draft_by_username(username, title, text):
    """
    Saves a user draft in the database.

    Args:
        username (str): The username.
        title (str): The draft title.
        text (str): The draft content.

    Returns:
        None

    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("SELECT Username FROM Users WHERE Username = ?", (username,))
    existing_user = cursor.fetchone()

    # Insert the new draft into the 'Users' table
    cursor.execute("INSERT INTO Users (Title, Draft) VALUES (?, ?)", (title, text))
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