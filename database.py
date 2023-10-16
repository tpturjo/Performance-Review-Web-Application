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
    cursor.execute("SELECT UserID FROM Users WHERE Username = ?", (user.get_user_name()))
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
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Execute the query
    cursor.execute('SELECT * FROM your_table WHERE ID=? AND password=?', (user_name, user_password))
    result = cursor.fetchone()

    # Close the connection
    conn.close()
    if result == None:
        return False
    else:
        return True


def get_user_data_by_id(UserID):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query
    cursor.execute('SELECT ID, name, password FROM user WHERE ID=?', (UserID,))
    user_data = cursor.fetchone()

    # Close the connection
    conn.close()
    # Returns user_data if successful. Return "None" if there is no such user_id
    return user_data if user_data else None




def save_user_draft_by_id(UserID):
    pass

def get_users_draft_by_id(UserID):
    pass

def publish(draft):
    # Write into database
    return