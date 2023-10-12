"""
Import statements for the Bottle web framework.
"""
from bottle import Bottle, request, run, template, static_file, redirect


app = Bottle()
@app.route('/')
def server():
    return static_file('index.html', root='./templates')

@app.route('/submit', method='POST')
def submit():
    """
    When <input type="submit" value="Submit"> is triggered from index.html, "username"
    is recieved by request.forms.

    "redirect" triggered /review, and passes username data to review() method.
    """
    username = request.forms.get('username')
    # Assuming you want to pass the username as a parameter to the second page
    redirect(f'/review?username={username}')


@app.route('/review')
def review():
    """
    "username" is reconstructed.
    return : review.html which is living in template folder
    """
    username = request.query.username
    return template('templates/review.html', username=username)

if __name__ == '__main__':
    HOST_NAME = 'localhost'
    SERVER_PORT = 8080
    run(app, host=HOST_NAME, port=SERVER_PORT, debug=True)