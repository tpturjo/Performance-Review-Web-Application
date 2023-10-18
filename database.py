from bottle import Bottle, request, run, template, static_file, redirect
import sqlite3

#Change this if database name is changed
database_name = 'userDatabase.db'

"""
THIS PROGRAM HANDLES ALL SQL LOGIC AND TRAFFIC
"""



#Input a user object [of type class User]
def create_user(user):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    print(user.get_user_name())
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
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query
    # cursor.execute("SELECT UserID FROM Users WHERE Username = ?", (user.get_user_name()))
    print("matching credentials")
    cursor.execute('SELECT * FROM Users WHERE Username=? AND password=?', (user_name, user_password))
    result = cursor.fetchone()

    # Close the connection
    conn.close()
    if result == None:
        return False
    else:
        return True

#
def get_user_data_by_id(UserID):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query
    cursor.execute('SELECT * FROM Users WHERE ID=?', (UserID,))
    user_data = cursor.fetchone()

    # Close the connection
    conn.close()
    # Returns user_data if successful. Return "None" if there is no such user_id
    return user_data if user_data else None

def get_user_data_by_username(user_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query
    cursor.execute('SELECT * FROM Users WHERE username=?', (user_name,))
    user_data = cursor.fetchone()

    # Close the connection
    conn.close()
    # Returns user_data if successful. Return "None" if there is no such user_id
    return user_data if user_data else None

def save_user_draft_by_username(username, title, text):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT Username FROM Users WHERE Username = ?", (username))
    existing_user = cursor.fetchone()

    # Insert the new user into the 'Users' table
    cursor.execute("INSERT INTO Users (Title, Draft) VALUES (?, ?)",
                   (title, text))
    conn.commit()
    conn.close()


def get_users_draft_by_id(username):

    pass


"""
    Args: 
        draft (type string)
    Return:
        NONE
    Details: 
        takes one draft and add it to "publish" database 
"""
def publish_review(username, title, content):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Reviews (Username, Title, Content) VALUES (?, ?, ?)", (username, title, content))
    conn.commit()
    conn.close()
    pass

"""
    Args :
        NONE
    Return :
        List of reviews
"""
def get_published_reviews():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query to get all reviews
    cursor.execute('SELECT * FROM Reviews')
    reviews_data = cursor.fetchall()

    # Close the connection
    conn.close()

    return reviews_data
    pass


