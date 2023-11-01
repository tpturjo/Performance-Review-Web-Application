from bottle import Bottle, request, run, template, static_file, redirect, response
import sqlite3
import app
import user
import database

app = Bottle()

"""
Services: File address reference for each HTML file  
"""


@app.route('/')
def login():
    """
    Serves the login page.

    Returns:
        str: The login page HTML.

    """
    return static_file('login.html', root='./templates')


@app.route('/public')
def public():
    """
    Serves the public page that displays all published reviews.

    Returns:
        str: The public page HTML.

    """
    all_published = database.get_published_reviews()
    all_published_reformatted = format_list_for_public(all_published)
    return template('templates/public.html', reviews=all_published_reformatted)


@app.route('/createAccount')
def create_account():
    """
    Serves the create account page.

    Returns:
        str: The create account page HTML.

    """
    return static_file('createAccount.html', root='./templates')


@app.route('/review')
def review():
    """
    Serves the review page.

    Returns:
        str: The review page HTML.

    """
    username = request.query.username
    username = request.get_cookie('username')
    data = database.get_user_data_by_username(username)
    text = data[2]
    return template('templates/review.html', username=username)


@app.route('/static/<filename>')
def serve_static(filename):
    """
    Serves static files.

    Args:
        filename (str): The name of the static file.

    Returns:
        str: The static file.

    """
    return static_file(filename, root='./templates')


@app.route('/submit', method='POST')
def submit():
    """
    Handles the form submission.

    Returns:
        str: The response HTML.

    """
    action = request.forms.get('action')

    if action == 'SAVE':
        pass

    elif action == 'PUBLISH':
        username = request.get_cookie('username')
        title = request.forms.get('title')
        text = request.forms.get('text')
        database.publish_review(username, title, text)
        return static_file('review.html', root='./templates')

    elif action == 'LOGIN':
        # Logic for login
        username = request.forms.get('username')
        password = request.forms.get('password')
        can_log = database.check_credentials(username, password)
        if can_log:
            response.set_cookie('username', username)
            return redirect(f'/review?username={username}')
        else:
            print("Wrong ID or Password")
            return static_file('login.html', root='./templates')

    elif action == 'CREATE':
        username = request.forms.get('username')
        password = request.forms.get('password')
        print("hi I'm in create")

        new_user = user.User(username, password)
        success = database.create_user(new_user)

        if success:
            print("Successfully created user")
            return static_file('login.html', root='./templates')
        else:
            print("ERROR: username already taken. Try again")
            return "Failure"  # This message will be received by JavaScript


def format_list_for_public(lst):
    """
    Formats the list of published reviews for the public page.

    Args:
        lst (list): The list of published reviews.

    Returns:
        list: The formatted list of reviews.

    """
    new_list = []
    for element in lst:
        new_tuple = []
        myString1 = "Author: " + handle_none_variables(element[0])
        myString2 = "Title: " + handle_none_variables(element[1])
        myString3 = "Content: " + handle_none_variables(element[2])
        new_tuple.append(myString1)
        new_tuple.append(myString2)
        new_tuple.append(myString3)
        new_list.append(new_tuple)
    return new_list



def handle_none_variables(element):
    """
    Handles None values by converting them to the string "none".

    Args:
        element: The value to handle.

    Returns:
        str: The converted value.

    """
    if element == None:
        return "none"
    else:
        return element


if __name__ == '__main__':
    HOST_NAME = 'localhost'
    SERVER_PORT = 8080
    run(app, host=HOST_NAME, port=SERVER_PORT, debug=True)
