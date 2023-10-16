"""
Import statements for the Bottle web framework.
"""
from bottle import Bottle, request, run, template, static_file, redirect
import sqlite3, app, user, database




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

        # username is a dummy variable pretend username works
        username = username
        # Logic for saving
        """ To implement
            - pull out draft belonging to the username  
            - spit out draft string; save it in a var which is ready for output. 
        """

        pass
    elif action == 'PUBLISH':
        # Logic for publishing
        pass
    elif action == 'LOGIN':
        # Logic for login
        canLogin = False
        username = request.forms.get('username')
        password = request.forms.get('password')
        database.get_user_data_by_id(username)


        """ To implement 
            - use the var username,password 
            - compare with data in SQL
            - if there is a match change canLogin to True
        """




        if(canLogin):
            redirect(f'/review?username={username}')

    elif action == 'CREATE':
        username = request.forms.get('username')
        password = request.forms.get('password')
        print("hi I'm in create")


        new_user = user.User(username, password)
        success = database.create_user(new_user)
        if(success):
            return static_file('login.html', root='./templates')
        else:
            print("ERROR: username already taken. Try again")
            return static_file('createAccount.html', root='./templates')





if __name__ == '__main__':
    HOST_NAME = 'localhost'
    SERVER_PORT = 8080
    run(app, host=HOST_NAME, port=SERVER_PORT, debug=True)