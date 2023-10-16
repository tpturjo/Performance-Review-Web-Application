from bottle import Bottle, request, run, template, static_file, redirect
import sqlite3

#Change this if database name is changed
database_name = 'userDatabase.db'


#Input a user object [of type class User]
def create_user(user):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT UserID FROM Users WHERE Username = ?", (user.get_user_name()))
    existing_user = cursor.fetchone()
    success = False
    if existing_user:
        conn.close()
        # return "Username already taken. Please choose a different one."
        success = False
    else:
        # Insert the new user into the 'Users' table
        cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", (user.get_user_name(), user.get_password()))
        conn.commit()
        conn.close()
        # return f"Registration successful for {username}"
        success = True



def get_user_data_by_id(user_id):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Execute the query
    cursor.execute('SELECT ID, name, password FROM user WHERE ID=?', (user_id,))
    user_data = cursor.fetchone()

    # Close the connection
    conn.close()
    # Returns user_data if successful. Return "None" if there is no such user_id
    return user_data if user_data else None

