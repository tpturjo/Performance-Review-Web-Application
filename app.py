from bottle import Bottle, request, run, template, static_file, redirect
import sqlite3, user, database

#pass in user object
# def login(user):
#     # Check if the username is already taken
#         conn = sqlite3.connect('userDatabase.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT UserID FROM Users WHERE Username = ?", (user.,))
#         existing_user = cursor.fetchone()
#
#         if existing_user:
#             conn.close()
#             # return "Username already taken. Please choose a different one."
#             return False
#         else:
#             # Insert the new user into the 'Users' table
#             cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", (username, password))
#             conn.commit()
#             conn.close()
#             # return f"Registration successful for {username}"
#             return True
