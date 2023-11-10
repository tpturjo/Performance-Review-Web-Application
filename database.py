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
       cursor.execute("UPDATE Drafts SET Title = ?, Content = ? WHERE Username = ?", (title, content, username))


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



def clear_drafts(username):
   """
      Remove draft entrie for a specified user from the database.

      This function connects to the SQLite database, delete records in the 'Drafts'
      table where the 'Username' matches the provided username, and then commits these changes.

      Parameters:
      username (str): The username for which  draft entries will be deleted.

      Returns:
      None: This function does not return anything.

      Note:
      This function will directly modify the 'Drafts' table in the database associated with the
      given 'database_name' global variable.
      """
   conn = sqlite3.connect(database_name)
   cursor = conn.cursor()

   cursor.execute("DELETE FROM Drafts WHERE Username = ?", (username,))

   # Commits the changes to the database
   conn.commit()
   # Closes the connection
   conn.close()


def save_rating(submission_id, rating):

   """
   Saves a rating for a specific review.

   Args:
       submission_id (int): The ID of the review.
       rating (float): The rating to be saved.

   Returns:
       None
   """
   conn = sqlite3.connect(database_name)
   cursor = conn.cursor()

   # Check if the review already has ratings
   cursor.execute("SELECT Accum_Ratings, Total_Ratings, Rating FROM Reviews WHERE Submission_ID = ?", (submission_id,))
   existing_data = cursor.fetchone()

   if existing_data:
      accum_ratings, total_ratings, current_rating = existing_data
      accum_ratings = 0 if accum_ratings is None else accum_ratings  # Handle None case
      total_ratings = 0 if total_ratings is None else total_ratings  # Handle None case
      total_ratings += 1

      if total_ratings != 0:
         average_rating = (accum_ratings + int(rating)) // total_ratings
      else:
         average_rating = 0

      cursor.execute("UPDATE Reviews SET Rating = ?, Accum_Ratings = ?, Total_Ratings = ? WHERE Submission_ID = ?",
                     (average_rating, accum_ratings + int(rating), total_ratings, submission_id))
   else:
      # If no ratings exist, insert a new record
      cursor.execute("INSERT INTO Reviews (Submission_ID, Rating, Accum_Ratings, Total_Ratings) VALUES (?, ?, ?, ?)",
                     (submission_id, int(rating), int(rating), 1))

   conn.commit()
   conn.close()


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
