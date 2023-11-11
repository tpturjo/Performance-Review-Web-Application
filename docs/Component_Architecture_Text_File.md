Component Architecture Document

THIS DOCUMENT WAS WRITTEN TOGETHER AS A TEAM VIA GOOGLE DRIVE

**Server App**
Route.py uses the Bottle framework to serve the server/webpage

**Session Management**
Session is mainly done via HTTP technology cookies from the user’s browser. 
Route.py flags cookies to be created, and it stores client’s user info. The cookie itself is the session control.  
“def require_login(func)” in route.py enforces unique sessions from the server side.

	
**Project Server**
submit/Save: This function handles form submissions. When a user saves a draft, their username, the draft's title, and 
text are saved to a database. It then retrieves all drafts for the user and displays them using a template.

public(): This function displays all published reviews. It can also filter these reviews based on a search query 
provided by the user. The function formats the retrieved reviews and sends them to a template for display.
	
@app.route('/')
def login():
Response Handler
Serves HTML file

@app.route('/changePassword')
@require_login
def change_password():
Response Handler
Serves HTML file

@app.route('/public')
def public():
Response Handler
Serves HTML file

@app.route('/createAccount')
def create_account():
Response Handler
Serves HTML file


@app.route('/review')
@require_login
def review():
Response Handler
Serves HTML file

@app.route('/static/<filename>')
def serve_static(filename):
Response Handler
Dynamic path for directories

@app.route('/static_img/<filename>')
def serve_static_img(filename):
Response Handler
Dynamic path for image directory

@app.route('/submit', method='POST')
def submit():
Request Handler
App Logic Module


**App Logic**
App logic is in route.py. It is part of the request handler. It is triggered by “POST” requests from the html side, 
which is detected by the bottle framework in route.py.

App logic realizes the features by interacting with the database, data structure, database
methods, and helper methods. All App logic can be found in route.py, under :
@app.route(‘/submit’, method=’post’)
@app.route('/change_password', method='POST')
@app.route('/rate', method='POST')
There are 7 unique app features:
1. SAVE
2.PUBLISH
3.LOGIN
4.CREATE
5.LOGOUT
6.change (change password)
7. rate 
They are triggered when the HTML page forms an “action” with a “method”.


**Helper Methods**
format_list_for_public(list): takes a list of user data retrieved from SQL. It appends strings to 
each element in the list for print

handle_non_variables(element): Sometimes the database might return null object. This is a helper method 
that handles that.

handle_reviews(element): Receives an integer value and returns a ‘star’ icon.


**HTML Construction**
Change Password.HTML serves a page where a user can input their username, old password and new password they 
want to update to.
	
	
Login.html:
	Contains 
“Home” button: http request for path to login.html
“Write a review” button:  http request for path to review.html
	
Public.html:
On load, by default, route.py loads Public.html with data all the review data from SQL. 
Data is loaded in the html lines:
               <h5 id="title">{{ review[1] }}</h5>
                            <h5>{{ review[0] }}</h5>
                            <h5>{{ review[2] }}</h5>
                            <h5>{{ review[3] }}</h5> 

 “Home” button: http request for path to login.html

“Write a review” button:  http request for path to review.html

“⭐️⭐️⭐️⭐️⭐️” button: invokes request handler, which is passed on to route.py app logic to interact with the database. 

'share-button'. When a share button is clicked, it retrieves the review's title and content from the button's data 
attributes and creates a shareable text. If the Web Share API is supported by the user's device or browser, 
it enables sharing this text along with a URL; if not, it displays an alert indicating that sharing is not supported. 

Search function: The form sends a GET request to the /public endpoint with the user's input from a text field named 'search', 
which is used for searching by author or title. The text field is pre-populated with any existing search query 
({{search_query}}), and there's a submit button labeled "Search". 


review.Html:
Save Button: The 'SAVE' button in the form sends a POST request to the /submit endpoint with the entered review title 
and text, allowing the user to save the current draft of their review.

styles.css: 
Styling of the HTML components.			

**Object Mapping**
def create_user(user): Creates a new user in the database.

def check_credentials(user_name, user_password): Checks the credentials of a user.

def get_user_data_by_username(user_name): Retrieves user data from the database by username.

def publish_review(username, title, content): Publishes a review by adding it to the 'Reviews' table in the database.

def get_published_reviews(): Retrieves all published reviews from the 'Reviews' table in the database.

def get_users_published_reviews(username): Retrieves the user's published reviews from the 'Reviews' table in the database.

def save_draft(username, title, content): Saves a draft review instead of publishing it publicly.

def get_drafts(username): Retrieves the user's saved drafts from the 'Drafts' table in the database.

def clear_drafts(username): The clear_drafts function takes a username as a parameter and delete draft entrie associated 
with that username from the database.Our user objects accessed all the attributes and inherited some of the methods from 
our model. 

def save_rating(submission_id, rating): Saves a rating, number of ratings, and sum of all rating values submitted for 
a specific review. Also calculates average of ratings submitted on a review.

def change_password(username, new_password): Processes the change password form and updates the user's password.

**Data Structure**
User.py holds the model for the User Class. It has getters and setters, and it prepares the data to be stored 
into the database tables. 


**Data Store**
All data is stored in the userDatabase.db file.

It contains the following tables:

Users table: Includes primary key Username and attribute for password

Reviews table: Includes primary key Submission_ID, foreign key Username, Title (review titles),
Content (published reviews), Rating (holds the average of a review’s ratings),
Accum_Ratings (holds the sum of rating values submitted), Total_Ratings (holds the sum of each individual rating)

Draft table: Includes primary key Draft_ID, foreign key Username, Title (draft titles), Content (published reviews)
