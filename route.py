from bottle import Bottle, request, run, template, static_file, redirect, response
import sqlite3
import methods
import user
import profile
import database

app = Bottle()


def require_login(func):
    """
    Flow control. Blocks the use of any service if a cookie is not present.

    Returns:
        str: If no cookies present returns the login page HTML. Else proceed with flow.
    """

    def wrapper(*args, **kwargs):
        if request.get_cookie('username'):
            return func(*args, **kwargs)
        else:
            return redirect('/')  # Redirect to login page if not logged in

    return wrapper

def require_logout(func):
    """
    Flow control. Blocks the use of LOGIN page when already logged in.

    Returns:
        str: If cookie is present, block the access of LOGIN page.
    """
    def wrapper(*args, **kwargs):
        mysring = request.get_cookie('username')
        if request.get_cookie('username') == None:
            return func(*args, **kwargs)
        else:
            return redirect('/')
    return wrapper

"""
Services: File address reference for each HTML file  
"""


@app.route('/')
def home():
    """
    Serves the login page.

    Returns:
        str: The login page HTML.

    """
    username = request.get_cookie('username')
    return template('templates/home.html', username=username)

@app.route('/login')
@require_logout
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
    Serve the public page displaying all published reviews.

    This function retrieves all published reviews from the database. If a search query
    is provided in the request, it filters the reviews based on this query. The reviews are
    then formatted for display and the public page HTML is returned with the reviews data.

    Returns:
        str: HTML content for the public page, including the list of reviews and the search query, if any.

    Notes:
        - The search query is case-insensitive and can match either the title or the content of the reviews.
        - Reviews are retrieved from the database using 'database.get_published_reviews()' and formatted with
          'methods.format_list_for_public()'.
        - The template 'templates/public.html' is used to render the HTML content.
    """
    search_query = request.query.get('search')
    all_published = database.get_published_reviews_and_comments()
    if search_query:
        # Filter the reviews based on the search query
        filtered_reviews = [review for review in all_published if
                            (review[1] is not None and search_query.lower() in review[1].lower()) or
                            (review[2] is not None and search_query.lower() in review[2].lower())]
        all_published_reformatted = methods.format_list_with_comments_for_public(filtered_reviews)
    else:
        all_published_reformatted = methods.format_list_with_comments_for_public(all_published)
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


@app.route('/profileEdit')
def profileEdit():
    """
    Serves the profile edit page.

    This page allows users to view and edit their profile information.

    Returns:
        str: The rendered profile edit page template with the user's profile data.
    """
    username = request.get_cookie('username')
    profile_data = database.get_profile_data_by_username(username)
    return template('templates/profile_edit.html', username=username, profile_data=profile_data)

@app.route('/profile')
def profilePage():
    """
    Serves the profileEdit page.

    Returns:
        str: The review page HTML.

    """
    username = request.get_cookie('username')
    profile_data = database.get_profile_data_by_username(username)
    return template('templates/profile.html', username=username, profile_data=profile_data)


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
        database.clear_drafts(username)
        draft_data = None
        return template('templates/review.html', username=username, draft_data=draft_data,
                        saved_message="Review published successfully")

    elif action == 'COMMENT':
        submission_id = request.forms.get('submission_id')
        username = request.get_cookie('username')
        comment = request.forms.get('comment')
        database.save_comment(submission_id, username, comment)
        redirect('/public')

    elif action == 'LOGIN':
        # Logic for login
        username = request.forms.get('username')
        password = request.forms.get('password')
        can_log = database.check_credentials(username, password)
        if can_log:
            response.set_cookie('username', username)
            return redirect(f'/review?username={username}')
        else:
            return template('templates/login.html', message="Incorrect username or password")

    elif action == 'CREATE':
        username = request.forms.get('username')
        password = request.forms.get('password')
        new_user = user.User(username, password)
        success = database.create_user(new_user)

        if success:
            print("Successfully created user")
            return static_file('login.html', root='./templates')
        else:
            print("Username already taken. Try again")
            return "Failure"  # This message will be received by JavaScript

    elif action == 'EDIT_PROFILE':
        username = request.get_cookie('username')
        my_profile = profile.Profile(username)
        my_profile.set_first_name(request.forms.get('first_name'))
        my_profile.set_last_name(request.forms.get('last_name'))
        my_profile.set_email(request.forms.get('email'))
        my_profile.set_address(request.forms.get('address'))
        database.edit_profile(username, my_profile)
        redirect('/profile')

    elif action == 'LOGOUT':
        username = request.get_cookie('username')
        # response.delete_cookie(username)
        response.set_cookie("username", '', expires=0)
        return template('templates/login.html', message=None)

    elif action == 'ANONYMOUS':
        username = 'Anonymous'
        title = request.forms.get('title')
        text = request.forms.get('text')

        # Saves the review using an anonymous username
        database.publish_review(username, title, text)

        # Clears drafts
        database.clear_drafts(username)

        # Redirects to public
        return redirect('/public')

@app.route('/change_password', method='POST')
def change():
    """
        Handles the change password page.



        Returns:
            link: to the login page and changed password successfully or wrong credeentials according to user's response.

        """
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
            return template('templates/changePassword.html', message="Wrong Credentials")


@app.route('/rate', method='POST')
def rate():
    """
    Handles the form submission of rate.
    NOTE: This was taken out of submit() due to too many if statements.


    Returns:
        link: Route to an HTML service.

    """

    # Logic for updating review.
    review_id = request.forms.get('review_id')
    rating = request.forms.get('rating')

    if rating == '1':
        database.save_rating(review_id, 1)
        redirect('/public')
    elif rating == '2':
        database.save_rating(review_id, 2)
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


@app.route('/my_posts')
@require_login
def my_posts():
    """
        Serves the page displaying all posts made by the logged-in user.

        Retrieves and displays all reviews published by the user.

        Returns:
            str: The rendered template displaying the user's posts.
    """
    username = request.get_cookie('username')
    user_reviews = database.get_users_published_reviews(username)
    return template('templates/my_posts.html', reviews=user_reviews, username=username)

@app.route('/edit_post/<post_id>', method='POST')
@require_login
def edit_post(post_id):
    """
        Handles the editing of an existing post.

        Allows users to update the title and content of their posts. Unauthorized access attempts are blocked.

        Args:
            post_id (str): The ID of the post to be edited.

        Returns:
            Redirect or str: A redirect to the 'my_posts' page after successful editing, or a failure message.
    """
    username = request.get_cookie('username')
    post = database.get_post_by_id(post_id)
    if post and post[1] == username:
        title = request.forms.get('title')
        content = request.forms.get('content')
        database.update_post(post_id, title, content)
        return redirect('/my_posts')
    else:
        return "Unauthorized access"



if __name__ == '__main__':
    HOST_NAME = 'localhost'
    SERVER_PORT = 8080
    run(app, host=HOST_NAME, port=SERVER_PORT, debug=True)