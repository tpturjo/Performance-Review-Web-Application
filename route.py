"""
Import statements for the Bottle web framework.
"""
from bottle import Bottle, request, run, template, static_file, redirect


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
@app.route('/makeAccount')
def public():
    return static_file('makeAccount.html', root='./templates')
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
        pass
    elif action == 'PUBLISH':
        # Logic for publishing
        pass
    elif action == 'LOGIN':
        # Logic for login
        username = request.forms.get('username')
        redirect(f'/review?username={username}')
    else:
        # Handle other cases
        pass






if __name__ == '__main__':
    HOST_NAME = 'localhost'
    SERVER_PORT = 8080
    run(app, host=HOST_NAME, port=SERVER_PORT, debug=True)