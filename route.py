"""
Import statements for the Bottle web framework.
"""
from bottle import Bottle, request, run, template, static_file, redirect
import sqlite3, app


app = Bottle()
"""
Services: File address reference for each HTML file  
"""
@app.route('/')
def server():
    return static_file('login.html', root='./templates')
@app.route('/public')
def public():
    return static_file('public.html', root='./templates')
@app.route('/createAccount')
def public():
    return static_file('createAccount.html', root='./templates')
@app.route('/review')
def review():
    username = request.query.username
    return template('templates/review.html', username=username)
@app.route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='./templates')


@app.route('/submit', method='POST')
def submit():
    # username = request.forms.get('username')
    # Assuming you want to pass the username as a parameter to the second page
    # redirect(f'/review?username={username}')
    action = request.forms.get('action')
    if action == 'SAVE':
        # Logic for saving
        print("hi")
        pass
    elif action == 'PUBLISH':
        # Logic for publishing
        pass
    elif action == 'LOGIN':
        # Logic for login
        username = request.forms.get('username')
        password = request.forms.get('password')
        redirect(f'/review?username={username}')
    elif action == 'CREATE':
        username = request.forms.get('username')
        password = request.forms.get('password')
        print("hi I'm in create")
        # success = app.createUser(username, password)


        # Check if the username is already taken
        conn = sqlite3.connect('userDatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT UserID FROM Users WHERE Username = ?", (username,))
        existing_user = cursor.fetchone()
        success = False
        if existing_user:
            conn.close()
            # return "Username already taken. Please choose a different one."
            success = False
        else:
            # Insert the new user into the 'Users' table
            cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            # return f"Registration successful for {username}"
            success = True
        print("Did it succeed?")
        print(success)
        if(success):
            return static_file('login.html', root='./templates')

    else:
        # Handle other cases
        pass




if __name__ == '__main__':
    HOST_NAME = 'localhost'
    SERVER_PORT = 8080
    run(app, host=HOST_NAME, port=SERVER_PORT, debug=True)