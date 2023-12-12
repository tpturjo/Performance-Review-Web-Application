# Component Architecture Document

The component architecture of this web application delineates a clear separation of concerns, dividing functionality into distinct, manageable parts that interact with each other through
well-defined interfaces. At its core, the architecture consists of a client-server model, with a relational database for persistent storage. The server handles HTTP requests, session management, 
and communicates with the database, which is structured to store users, profiles, reviews, drafts, and comments. This modular design not only promotes maintainability and scalability but also 
simplifies the process of testing and development by isolating individual components.
## Contents:
### UML Diagram
- Visual Representation Overview
### Components
- Client-Side: HTML & CSS
- Server-Side: HTTP Handlers & Logic
- Data Structures & Object Mapping
- Database & Session Management
- Utility Functions
### Testing Components
- API & Unit Testing Specifications
### Component Interaction
- Communication, Session, & Database Dynamics
### Module Interface
- Authentication, Profile, Review, Draft, & Comment Modules
### API Endpoints
- Description of Application Endpoints
### Assessment
- Usability, Maintainability, Testability, Scalability, Risk
### Conclusion
- Architectural Summary & Outlook
# UML Diagram:
![UML Diagram (Team M)1 ](https://github.com/CS2005F23/term-project-teamm/blob/master/docs/Asset/Final%20UML%20diagram.jpeg?raw=true)

## Components:

### 1. Client-Side Components:
HTML templates and CSS are used for the presentation layer of the application.

- changePassword.html: A template for the page where users can change their password.
- createAccount.html: A template for the page where new users can create an account.
- home.html: The main landing page of the website.
- login.html: A template for the login page.
- my_posts.html: A template showing a list of posts made by the logged-in user.
- profile.html: The user profile page.
- profile_edit.html: A template for editing user profile details.
- public.html: A page displaying public posts or information.
- review.html: A template for the review page where users can write and submit reviews.
- styles.css: The stylesheet defining the look and feel of the website.
### 2. Server-Side Components (server.py):
- Functions that handle HTTP requests and interact with the back-end logic.
- require_login(func): Decorator to enforce user login for certain routes.
- require_logout(func): Decorator to restrict access to login page for authenticated users.
- home(): Serves the home/login page.
- login(): Displays the login page.
- change_password(): Shows the change password page.
- public(): Renders the public page with reviews and optional search.
- create_account(): Serves the account creation page.
- review(): Shows the review submission page with drafts.
- profileEdit(): Renders the profile editing page.
- profilePage(): Displays the profile page.
- serve_static(filename): Serves static files from the server.
- serve_static_img(filename): Serves static image files.
- submit(): Processes form submissions for various actions like save, publish, comment, login, create account, etc.
- change(): Handles password changes via form submission.
- rate(): Processes the rating of reviews.
- my_posts(): Displays all posts made by the logged-in user.
- edit_post(post_id): Edits an existing post.

### 3.Data Structure:
Functions for manipulating the data structures within the application.

#### profile.py:
- Represents a user's profile information with getters and setters for first name, last name, email, and address.
 
#### user.py:
- User Class: Represents a user with methods to get and set username, password, and drafts.
- Draft Class: Represents a draft post with methods to set and get title and content.

### 4. Object Mapping (database.py):
Functions that map objects to database records for Create, read, update, and delete.
- create_user(user): Registers a new user in the database if the username doesn't exist.
- check_credentials(user_name, user_password): Validates a user's login credentials.
- get_user_data_by_username(user_name): Retrieves a user's data based on their username.
- publish_review(username, title, content): Adds a new review to the 'Reviews' table in the database.
- get_published_reviews(): Fetches all reviews from the 'Reviews' table.
- get_published_reviews_and_comments(): Gathers all reviews and their associated comments.
- get_users_published_reviews(username): Retrieves all reviews posted by a specific user.
- save_draft(username, title, content): Stores or updates a user's draft review.
- get_drafts(username): Fetches all draft reviews for a specific user.
- clear_drafts(username): Deletes all draft reviews for a specific user.
- save_rating(submission_id, rating): Records a rating for a given review.
- get_First_Name(first_name): Looks up users by their first name in the 'Profiles' table.
- set_First_Name(): Placeholder method intended to set a user's first name (unimplemented).
- save_comment(submission_id, username, content): Stores a new comment for a given review.
- get_comments(submission_id): Retrieves comments associated with a specific review.
- change_password(username, new_password): Updates a user's password.
- get_profile_data_by_username(username): Fetches profile data for a given username.
- edit_profile(username, profile): Updates a user's profile information.
- get_post_by_id(post_id): Gets a post by its ID from the 'Reviews' table.
- update_post(post_id, title, content): Modifies the title and content of a post.

### 5.Data Store (userDatabase.db):
The database component that stores various data entities.

- Users data: Contains user name and password for authentication.
- Pofile data: user's profile information(first name, last name, email, and address).
- Comments data: Holds data related to comments on  reviews.
- Reviews data: Contains reviews and rating made by users.
- Drafts data: Stores drafts of reviews that have not been published.

### 6.Session Management:
Manages user sessions through cookies, likely handling login sessions and maintaining state across HTTP requests.

### 7. Helper Methods (methods.py):
- Utility methods that provide additional functionality.
- format_list_for_public(list): Formats a list of reviews for public display.
- format_list_with_comments_for_public(list): Formats a list of reviews with comments for public display.
- handle_none_variables(element): Converts None values in an element to the string "none".
- handle_reviews(element): Returns a string representation of a numeric rating.

### 8.Testing Components:
#### API Tests(term-project-teamm.postman_collection.json):
Defined in a Postman collection, these tests validate the API endpoints for correctness.
- GET Initial: Tests the initial response from the server to ensure the API is up and reachable.
- GET Account: Validates retrieval of account details for logged-in users.
- POST Create Account with existed username: Checks that the account creation process prevents duplicate usernames.
- POST Create Account with new username: Confirms that new users can create an account with a unique username.
- POST Log in with false username: Tests login with invalid credentials to ensure it fails as expected.
- POST Log in with correct username: Validates successful login with valid user credentials.
- POST Publish Review: Ensures that authenticated users can publish reviews.
- POST Publish Anonymous Review: Checks the ability to publish reviews anonymously.
- POST Save Draft: Tests saving drafts for authenticated users.
- POST Change Password: Validates password changes for existing users.
- POST Log Out: Ensures users can log out and end their session.
- POST Log in with new pass and Draft: Verifies login with new credentials and draft access.
- GET Profile page: Retrieves the profile page for the logged-in user.
- POST Edit Profile page: Confirms profile edits are applied and stored.
- GET Updated profile page: Retrieves the profile page to confirm updates.
- GET My Posts page: Validates that a user can retrieve a list of their posts.
- POST Edit existing post: Checks the ability to edit an existing post.
- GET Public Review Feed: Tests retrieval of the public feed of reviews.
- GET Search Function of Public Page: Validates the search functionality on the public reviews page.
- GET Rating functionality check: Confirms that the review rating functionality is working.
- POST create a comment on a post: Tests the ability to add comments to a post. 
- GET view comment: Validates the retrieval of comments for a post
#### Unit Tests (unit_test.py):
These tests ensure that the individual units of code work as expected, covering a range of methods from user creation to data retrieval and modification.
- setUp(self): Initializes the database, creates necessary tables, and sets up a test user for the tests.

- tearDown(self): Closes the database connection and removes the test database after each test.

- test_create_user(self): Ensures that a new user can be created and returns True if successful.

- test_get_user_data_by_username(self): Checks that user data can be correctly retrieved by username.

- test_get_user_data_by_nonexistent_username(self): Verifies that querying a non-existent username returns None.

- test_duplicate_user_creation(self): Confirms that creating a user with an existing username returns False.

- test_check_credentials(self): Tests that valid user credentials are accepted and invalid ones are rejected.

- test_check_wrong_credentials(self): Ensures that incorrect credentials for an existing user return False.

- check_credentials(self, user_name, user_password): Helper method to check if user credentials are valid within the test class.

- test_publish_review(self): Verifies that a review can be published and is retrievable from the database.

- test_get_published_reviews(self): Ensures that all published reviews can be retrieved from the database.

- test_get_comments(self): Checks that comments are correctly retrieved for a specific review.

- test_get_comments_for_review_with_no_comments(self): Ensures that no comments are returned for a review that has none.

- test_save_comment(self): Confirms that a comment can be saved for a specific review.

- test_save_multiple_comments_for_same_review(self): Checks that multiple comments can be saved and retrieved for the same review.

- test_change_password(self): Tests the functionality to change a user's password and validates the update.

- test_save_rating(self): Verifies that a rating can be saved for a review and is stored correctly.

- test_save_multiple_ratings_for_same_review(self): Ensures that multiple ratings for the same review are correctly averaged and stored.

- test_get_users_published_reviews(self): Confirms that all reviews published by a specific user can be retrieved.

- test_get_users_published_reviews_for_user_with_no_reviews(self): Checks that no reviews are retrieved for a user who has published none.

- test_get_first_name_for_nonexistent_name(self): Verifies that searching for a non-existent first name returns no results.

- test_clear_drafts(self): Tests that clearing drafts removes all drafts for a user.

- test_update_post(self): Checks that updating a post's title and content works correctly and persists changes.

- test_edit_nonexistent_review(self): Ensures that attempting to edit a non-existent review has no effect.

- test_edit_profile(self): Tests that the edit_profile function updates a user's profile information correctly.

## Component Interaction:
### 1.Client-Server Communication: 
The client (user's browser) interacts with the server by sending HTTP requests for pages like login, profile, 
and review submission. The server, using the Bottle framework, processes these requests and returns the appropriate HTML pages or API responses.
### 2.Session Management: 
During interactions that require authentication, such as profile editing or review submission, the server manages sessions, likely utilizing cookies to maintain 
state and ensure that requests are authenticated.
### 3.Database Interactions:
When the server processes requests that require data retrieval or modification (e.g., creating an account, publishing a review, editing a profile), it communicates with 
the SQLite database through the database interface, which performs the necessary SQL operations.
### 4.Data Structure Manipulation: 
The server-side logic, upon receiving data from the client (like a new review or a profile update), uses defined data structures to validate and organize the data before
it is sent to the database for storage.
### 5.API Endpoint Usage: 
For actions initiated by the client that involve data manipulation, such as posting comments or changing passwords, the client interacts with specific API endpoints that invoke the corresponding
server logic to process these actions.
### 6.Testing and Validation: 
 The application includes a suite of tests to ensure that all parts of the system are functioning correctly. Unit tests in test_unit.py validate the logic of individual components, while API tests check 
 the end-to-end functionality of API endpoints, verifying that the server correctly processes requests and interacts with the database as expected.
### 7.Security Enforcement:
Security measures are integrated into the application, with components like the login system checking credentials against stored data in the database and handling password changes, ensuring secure user access.
### 8.Profile and Review Management:
The application's functionality for managing user profiles and reviews involves the client requesting to view or edit their data, the server handling these requests, and the database updating or retrieving
profile and review information as needed.
### 9.Content Creation and Draft Saving: 
When users create content (reviews or drafts), the server processes these creations, temporarily storing them as drafts if needed, or committing them to the database as public reviews.

## Module interface:
### 1.Authentication Module:
- Interfaces: Functions for login, logout, password change.
- Consistency: Uses session management for maintaining user state across requests.
- Docstrings: Descriptions for each function detail the expected inputs, outputs, and side effects.
- Unit Tests: Cover scenarios including successful login, failed login attempts, and session persistence.
### 2.Profile Management Module:
- Interfaces: Functions for retrieving and updating user profile data.
- Consistency: Interacts directly with the Profiles table in the database.
- Docstrings: Each method includes details on the parameters, return types, and any exceptions thrown.
- Unit Tests: Validate profile retrieval, updates, and error handling for non-existent profiles.
### 3.Review Management Module:
- Interfaces: Provides methods for creating, retrieving, and updating reviews.
- Consistency: Works with the Reviews database table, ensuring data integrity.
- Docstrings: Clearly outlines the purpose and usage of each method, including database interactions.
- Unit Tests: Test creation of reviews, retrieval of existing reviews, and proper handling of updates.
### 4.Anonymous Review Module:
- Interfaces: Methods for submitting reviews without revealing user identity.
- Consistency: Interacts with the Reviews table but does not store user-related data.
- Docstrings: Describe functionality for submitting an anonymous review and expected behavior.
- Unit Tests: Test that reviews are posted without user information and are retrievable publicly.
### 5.Draft Management Module:
- Interfaces: Includes methods for saving, editing, and deleting draft content.
- Consistency: Manages drafts in line with the Drafts table structure and relationships.
- Docstrings: Provides comprehensive information on how to use the methods and expected results.
- Unit Tests: Ensures drafts are saved and retrieved correctly, and that edits and deletions work as intended.
### 6.Comment Management Module:
- Interfaces: Functions for adding comments to reviews and fetching comments.
- Consistency: Aligns with the Comments table schema for storing and retrieving comment data.
- Docstrings: Describes parameters, return information, and any database transactions performed.
- Unit Tests: Checks the creation of comments, their association with the correct reviews, and retrieval accuracy.
### 7.Profile Information Module:
- Interfaces: Provides access to personal and account-related information for a user's profile.
- Consistency: Directly corresponds with the Profiles database table and user session data.
- Docstrings: Detailed information on retrieving and updating profile data, including constraints and permissible values.
- Unit Tests: Ensure accurate retrieval and secure updating of profile information, with appropriate authentication checks.
### 8.Rating Review Module:
- Interfaces: Contains methods to submit and manage ratings for reviews.
- Consistency: Works in tandem with the Reviews table, particularly focusing on updating the rating-related fields (like Rating, Accum_Ratings, and Total_Ratings).
- Docstrings: Each function in the module is documented with clear descriptions, explaining how ratings are submitted, updated, and how average ratings are calculated.
- Unit Tests: The testing suite would include scenarios to ensure ratings are accurately recorded and updated. This would involve testing individual rating submissions, checking the calculation of average ratings, and verifying that ratings are properly reflected on the review.
### 9.Search Module:
- Interfaces: Search functions to query username or Title based on user input.
- Consistency: Utilizes database indexing and query optimization for efficient search.
- Docstrings: Details the search criteria, usage, and how the search results are returned.
- Unit Tests: Validates the accuracy and relevance of search results, and ensures no unauthorized data is returned.
### 10.Share Review Module:
- Interfaces: Methods to share reviews on external platforms or within the application.
- Consistency: Ensures shared content matches the original content and retains link back to the source.
- Docstrings: Explains the sharing mechanism, expected inputs like review identifiers, and output results.
- Unit Tests: Confirms that sharing functionality exposes only the intended data and respects privacy settings.

## API Endpoint of application:
### 1.POST /createAccount
- Purpose: Registers a new user.
- Input: Username, password.
- Output: Success message or error.
### 2.POST /login
- Purpose: Authenticates a user.
- Input: Username, password.
- Output: Session token or error.
### 3.POST /changePassword
- Purpose: Allows users to change their password.
- Input: Old password, new password.
- Output: Success or failure message.
### 4.POST /submit (action='LOGOUT')
- Purpose: Logs out the current user.
- Output: Confirmation of logout.
### 5.GET /profile
- Purpose: Retrieves the profile information of the logged-in user.
- Output: User profile data.
### 6.POST /profileEdit
- Purpose: Updates the user’s profile information.
- Input: Updated profile data.
- Output: Confirmation of update.

### 7.POST /submit (action='PUBLISH')
- Purpose: Publishes a new review.
- Input: Review content.
- Output: Success or failure message.
### 8.POST /submit (action='SAVE')
- Purpose: Saves a review draft.
- Input: Draft content.
- Output: Confirmation of save.
### 9.GET /public
- Purpose: Retrieves all public reviews.
- Output: List of reviews.
### 10.POST /submit (action='COMMENT')
- Purpose: Adds a comment to a review.
- Input: Review ID, comment content.
- Output: Success or failure message.
### 11.POST /rate
- Purpose: Submits a rating for a review.
- Input: Review ID, rating value.
- Output: Updated rating.
### 12.POST /submit (action='ANONYMOUS')
- Purpose: Publishes a review anonymously.
- Input: Review content.
- Output: Success or failure message.

### 13. POST /edit_post/<post_id>
- Purpose: Edits an existing review or draft.
- Input: Post ID, updated content.
- Output: Success or failure message.
## Assessment of Qualities
### Usability:
The application's client-side components, such as HTML templates and CSS, provide a clear and consistent user interface. The separation into distinct pages like login, profile editing, and review 
submission supports a user-friendly experience. The use of AJAX for API interactions will likely improve the responsiveness and provide a seamless user experience by minimizing page reloads.

### Maintainability:
The modularity of the server-side components and clear separation of concerns enhance maintainability. Each module, such as session management and object mapping, is responsible for distinct 
functionality, allowing developers to update individual parts without affecting the whole. Docstrings and consistent coding practices across modules contribute to easier understanding and
maintenance of the codebase.

### Testability:
With a comprehensive suite of API and unit tests, the application demonstrates strong testability. The Postman collection allows for end-to-end testing of API endpoints, while the unit tests in
unit_test.py ensure that individual functions behave as expected. The modular design allows for isolated testing of components, which is a best practice for ensuring reliable software.

### Scalability:
The application's server-side components are designed to handle HTTP requests efficiently, which is a positive indicator for scalability. However, the scalability of the application would depend on 
the underlying database's ability to handle increased loads and the server framework's capability to manage concurrent sessions. The ability to scale up individual components or services would also 
be crucial as user demand grows.

### Risk:
There are a few risks to consider. First, the reliance on a relational database requires careful management of schema migrations and data integrity. Second, session management must be secure to 
prevent unauthorized access. Third, as the system scales, the server's ability to handle an increasing number of requests without performance degradation will be essential. Lastly, the current structure suggests a monolithic application, which may not be as resilient or easy to scale as a microservices architecture.

## Conclusion:
The web application's component architecture is well-structured, with a focus on separation of concerns and modularity, which bodes well for maintainability and testability. Usability is supported
by a straightforward client-side design, though actual user experience would need to be validated with user testing. Scalability is indicated but not fully detailed, suggesting a potential area for
future enhancement. Risks are present but manageable with proper attention to security and performance. Overall, the architecture provides a solid foundation, with room for improvements as the 
application evolves and scales.