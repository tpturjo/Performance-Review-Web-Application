from bottle import Bottle, request, run, template, static_file, redirect
import sqlite3
from methods import *

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

'''
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

    cursor.execute("SELECT Username FROM Drafts WHERE Username = ?", (username,))
    existing_user = cursor.fetchone()

    # Insert the new draft into the 'Users' table
    cursor.execute("INSERT INTO Users (Title, Draft) VALUES (?, ?)", (title, text))
    conn.commit()
    conn.close()
'''

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

    # Commits the changes to the database
    conn.commit()

    # Closes the connection
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


def get_users_published_reviews(username):
    """
        Retrieves the user's published reviews from the 'Reviews' table in the database.

        Returns:
            list: List of reviews (tuples) if successful.

        """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query to get all reviews
    cursor.execute("SELECT * FROM Reviews WHERE Username = ?", (username,))
    reviews_data = cursor.fetchall()

    # Close the connection
    conn.close()
    # Returns all of the user's reviews
    return reviews_data


"""
Draft Methods
"""

def save_draft(username, title, content):
    """
    Saves a draft review instead of publishing it publicly.
    Args:
        username: The username
        title: The title of the draft
        content: The content of the draft
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Drafts WHERE Username = ?", (username,))
    current_draft = cursor.fetchone()[0]

    if current_draft > 0:
        cursor.execute("UPDATE Drafts SET Title = ?, Content = ?, WHERE Username = ?", (title, content, username))

    else:
        cursor.execute("INSERT INTO Drafts (Username, Title, Content) VALUES (?, ?, ?)", (username, title, content))

    # Commits the changes to the database
    conn.commit()
    # Closes the connection
    conn.close()


def get_drafts(username):
    """
        Retrieves the user's saved drafts from the 'Drafts' table in the database.

        Returns:
            list: List of drafts (tuples) if successful.

        """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query to get all saved drafts
    cursor.execute('SELECT * FROM Drafts WHERE Username = ?', (username,))
    drafts_data = cursor.fetchall()

    #Closes the connection
    conn.close()
    #Returns all of the user's drafts
    return drafts_data

def save_rating(submission_id, username, rating):
    """
            Saves a review's rating score when a user rates a review.
    """

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Ratings(Submission_ID, Username, Rating) VALUES (?, ?, ?)", (submission_id, username, rating))

    # Commits the changes to the database
    conn.commit()
    # Closes the connection
    conn.close()


def get_average_rating(submission_id):
    """
        Calculates the average rating for a specific review.

        Args:
            Submission_ID INT - The ID of the review.

        Returns:
            The average of all ratings of a review.
        """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("SELECT Rating FROM Ratings WHERE Submission_ID = ?", (submission_id,))
    allRatings = cursor.fetchall()

    conn.close()

    return average_ratings(allRatings)


