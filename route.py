"""
Import statements for the Bottle web framework.
"""
from bottle import Bottle, request, run, template, static_file


app = Bottle()
@app.route('/')
def server():
    return static_file('index.html', root='./templates')

if __name__ == '__main__':
    HOST_NAME = 'localhost'
    SERVER_PORT = 8080
    run(app, host=HOST_NAME, port=SERVER_PORT, debug=True)