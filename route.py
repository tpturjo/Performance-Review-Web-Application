"""
Import statements for the Bottle web framework.
"""
from bottle import Bottle, request, run, template, static_file


app = Bottle()
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Performance Review</title>
</head>
<body>
    <h1>Welcome to the Performance Review App!</h1>
</body>
</html>

"""
@app.route('/')
def server():
    return HTML_TEMPLATE
if __name__ == '__main__':
    HOST_NAME = 'localhost'
    SERVER_PORT = 8080
    run(app, host=HOST_NAME, port=SERVER_PORT, debug=True)