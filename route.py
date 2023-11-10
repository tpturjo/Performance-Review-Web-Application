from bottle import Bottle, request, run, template, static_file, redirect, response
import sqlite3
import methods
import user
import database

app = Bottle()


def require_login(func):
    def wrapper(*args, **kwargs):
        if request.get_cookie('username'):
            return func(*args, **kwargs)
        else:
            return redirect('/')  # Redirect to login page if not logged in
    return wrapper

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
    return template('templates/login.html', message=None)


@app.route('/changePassword')
@require_login
def change_password():
    """
    Serves the change password page.

    Returns:
        str: The change password page HTML.

    """
    return template('templates/changePassword.html', message=None)


@app.route('/public')
def public():
    """
    Serves the public page that displays all published reviews.

    Returns:
        str: The public page HTML.

    """
    search_query = request.query.get('search')
    all_published = database.get_published_reviews()
    if search_query:
        # Filter the reviews based on the search query
        filtered_reviews = [review for review in all_published if
                            search_query.lower() in review[1].lower() or search_query.lower() in review[2].lower()]
        all_published_reformatted = methods.format_list_for_public(filtered_reviews)
    else:
        all_published_reformatted = methods.format_list_for_public(all_published)
    return template('templates/public.html', reviews=all_published_reformatted, search_query=search_query)


@app.route('/createAccount')
def create_account():
    """
    Serves the create account page.

    Returns:
        str: The create account page HTML.

    """
    return static_file('createAccount.html', root='./templates')


@app.route('/review')
@require_login
def review():
    """
    Serves the review page.

    Returns:
        str: The review page HTML.

    """
    username = request.get_cookie('username')
    draft_data = database.get_drafts(username)

    return template('templates/review.html', username=username, draft_data=draft_data)


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

@app.route('/static_img/<filename>')
def serve_static_img(filename):
    """
    Serves static files.

    Args:
        filename (str): The name of the static file.

    Returns:
        str: The static file.

    """
    return static_file(filename, root='./templates/img')


@app.route('/submit', method='POST')
def submit():
    """
    Handles the form submission.


    Returns:
        link: Route to an HTML service.

    """
    action = request.forms.get('action')

    if action == 'SAVE':
        username = request.get_cookie('username')
        title = request.forms.get('title')
        text = request.forms.get('text')
        database.save_draft(username, title, text)
        draft_data = database.get_drafts(username)
        return template('templates/review.html', username=username, draft_data=draft_data,
                        saved_message="Draft saved successfully")

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
            return template('templates/login.html', message = "Incorrect username or password")

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

    elif action == 'LOGOUT':
        print("attept to destroy cookie")
        username = request.get_cookie('username')
        print("attept to destroy cookie", username)
        # response.delete_cookie(username)
        response.set_cookie("username", '', expires=0)

        print("cookie destroyed")
        return template('templates/login.html', message=None)

@app.route('/change_password', method='POST')
def change():
    action = request.forms.get('action')
    if action == 'Change' or action == 'Change+':
        username = request.forms.get('username')
        current_password = request.forms.get('current-password')
        new_password = request.forms.get('new-password')
        login_status = database.check_credentials(username, current_password)
        if login_status:
            database.change_password(username, new_password)
            print("successfully changed password")
            return template('templates/changePassword.html', message="SUCCESS")
        else:
            print("Wrong credentials")
            return template('templates/changePassword.html', message = "Wrong Credentials")

@app.route('/rate', method='POST')
def rate():
    review_id = request.forms.get('review_id')
    rating = request.forms.get('rating')

    if rating == '1':
        database.save_rating(review_id, 1)
        redirect('/public')
    elif rating == '2':
        database.save_rating(review_id,2)
        redirect('/public')
    elif rating == '3':
        database.save_rating(review_id, 3)
        redirect('/public')
    elif rating == '4':
        database.save_rating(review_id, 4)
        redirect('/public')
    elif rating == '5':
        database.save_rating(review_id, 5)
        redirect('/public')


if __name__ == '__main__':
    HOST_NAME = 'localhost'
    SERVER_PORT = 8080
    run(app, host=HOST_NAME, port=SERVER_PORT, debug=True)
