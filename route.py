"""
Import statements for the Bottle web framework.
"""
from bottle import Bottle, request, run, template, static_file, redirect, response
import sqlite3, app, user, database




app = Bottle()
"""
Services: File address reference for each HTML file  
"""
@app.route('/')
def login():
    return static_file('login.html', root='./templates')
@app.route('/public')
def public():
    all_published = database.get_published_reviews()
    # for article in all_published:
    all_published = database.get_published_reviews()
    print(all_published)
    all_published_reformatted = format_list_for_public(all_published)
    print(all_published_reformatted)
    return template('templates/public.html', reviews=all_published_reformatted)
    # return static_file('public.html', root='./templates')
@app.route('/createAccount')
def create_account():
    return static_file('createAccount.html', root='./templates')
@app.route('/review')
def review():
    username = request.query.username

    username = request.get_cookie('username')
    data = database.get_user_data_by_username(username)
    text = data[2]

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
        pass


    elif action == 'PUBLISH':
        username = request.get_cookie('username')
        # data = database.get_user_data_by_username(username)
        # text = data[2]
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

            # return redirect('/review')
        else:
            print("Wrong ID or Password")
            return static_file('login.html', root='./templates')

    elif action == 'CREATE':
        username = request.forms.get('username')
        password = request.forms.get('password')
        print("hi I'm in create")

        new_user = user.User(username, password)
        success = database.create_user(new_user)

        if(success):
            print("Successfully created user")
            return static_file('login.html', root='./templates')
        else:
            print("ERROR: username already taken. Try again")
            return "Failure"  # This message will be received by JavaScript
            # return static_file('createAccount.html', root='./templates')



def format_list_for_public(list):
    newList = []
    for element in list:
        newTuple = []
        myString1 = "Author: " + handle_none_variables(element[0])
        myString2 = "Title: " + handle_none_variables(element[1])
        myString3 = "Content: " + handle_none_variables(element[2])
        newTuple.append(myString1)
        newTuple.append(myString2)
        newTuple.append(myString3)
        newList.append(newTuple)
    return newList

def handle_none_variables(element):
    if element == None:
        return "none"
    else:
        return element



if __name__ == '__main__':
    HOST_NAME = 'localhost'
    SERVER_PORT = 8080
    run(app, host=HOST_NAME, port=SERVER_PORT, debug=True)