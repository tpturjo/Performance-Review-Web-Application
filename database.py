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
       cursor.execute("INSERT INTO Profiles(Username) VALUES (?)", (user.get_user_name(),))
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


def get_published_reviews_and_comments():
   """
       Retrieves all published reviews along with their associated comments from the database.

       Returns:
           list: A list of reviews, each extended with its associated comments.
   """
   reviews_data = get_published_reviews()
   list_2d = [list(row) for row in reviews_data]

   for i in range(len(reviews_data)):
      comments = get_comments(reviews_data[i][0])
      list_2d[i][5] = comments

   return list_2d



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



#Draft Methods


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

   # Commits the changes to the database
   conn.commit()
   # Closes the connection
   conn.close()


#Profile Table Methods

def get_First_Name(first_name):
   """
       Retrieves users from the Profiles table whose first name matches the given name.

       Args:
           first_name (str): The first name to search for.

       Returns:
           list: A list of users matching the given first name.
   """
   conn = sqlite3.connect(database_name)
   cursor = conn.cursor()

   # Execute the query to get all saved drafts
   cursor.execute('SELECT * FROM Profiles WHERE First_Name = ?', (first_name,))
   users_first_name = cursor.fetchall()

   # Closes the connection
   conn.close()
   # Returns all of a user's drafts
   return users_first_name

def set_First_Name():
   """
       Placeholder for a function to set the first name of a user. Currently unimplemented.

       Returns:
           None
   """
   pass



#Comments Table Methods
def save_comment(submission_id, username, content):
   """
     Saves a user's comment for a specific review.

     Args:
         submission_id (int): The ID of the comment.
         username (text): The user's username.
         content (text): The text content of the comment.
     Returns:
         None
     """
   conn = sqlite3.connect(database_name)
   cursor = conn.cursor()

   cursor.execute("INSERT INTO comments (submission_id, username, comment) VALUES (?, ?, ?)", (submission_id, username, content))

   # Commits the changes to the database
   conn.commit()
   # Closes the connection
   conn.close()

def get_comments(submission_id):
   """
      Retrieves a comment for a specific review.

      Args:
         submission_id (int): The ID of the comment.
         username (text): The user's username.
         content (text): The text content of the comment.
      Returns:
         the comment for a review
      """
   conn = sqlite3.connect(database_name)
   cursor = conn.cursor()

   # Execute the query to get all reviews
   cursor.execute("SELECT * FROM comments WHERE submission_id = ?", (submission_id,))
   review_comment = cursor.fetchall()

   # Closes the connection
   conn.close()
   # Returns all of a user's reviews
   return review_comment


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




def get_profile_data_by_username(username):
   """
       Retrieves profile data for a specific user from the Profiles table.

       Args:
           username (str): The username whose profile data is to be retrieved.

       Returns:
           list: A list containing the profile data of the user.
   """
   conn = sqlite3.connect(database_name)
   cursor = conn.cursor()

   # Execute the query to get all saved drafts
   cursor.execute('SELECT * FROM Profiles WHERE Username = ?', (username,))
   profile_data = cursor.fetchall()

   #Closes the connection
   conn.close()
   #Returns all of the user's drafts
   return profile_data

def edit_profile(username, profile):
   """
       Updates the profile information of a user in the Profiles table.

       Args:
           username (str): The username of the user whose profile is to be updated.
           profile (Profile): A profile object containing the updated profile information.

       Returns:
           None
   """
   conn = sqlite3.connect(database_name)
   cursor = conn.cursor()
   # Update the user's password in the database
   cursor.execute('UPDATE Profiles SET First_Name=?, Last_Name=?, Email=?, Address=?  WHERE Username=?',
                  (profile.get_first_name(), profile.get_last_name(), profile.get_email(), profile.get_address(), username))
   conn.commit()
   conn.close()


def get_post_by_id(post_id):
   """
       Retrieves a specific post from the Reviews table by its ID.

       Args:
           post_id (int): The ID of the post to retrieve.

       Returns:
           tuple: A tuple containing the post data, or None if no post is found.
   """
   conn = sqlite3.connect(database_name)
   cursor = conn.cursor()
   cursor.execute('SELECT * FROM Reviews WHERE Submission_ID = ?', (post_id,))
   post = cursor.fetchone()
   conn.close()
   return post


def update_post(post_id, title, content):
   """
       Updates the title and content of a specific post in the Reviews table.

       Args:
           post_id (int): The ID of the post to be updated.
           title (str): The new title for the post.
           content (str): The new content for the post.

       Returns:
           None
   """
   conn = sqlite3.connect(database_name)
   cursor = conn.cursor()
   cursor.execute('UPDATE Reviews SET Title = ?, Content = ? WHERE Submission_ID = ?', (title, content, post_id))
   conn.commit()
   conn.close()
