import unittest

from user import User


from profile import *
from database import *



def remove_test_user(user):
    """
        Remove a test user from the database.

        Args:
            user: User object to be removed
        """
    conn = sqlite3.connect('userDatabase.db')
    cursor = conn.cursor()
    username = user.get_user_name()

    try:
        cursor.execute("DELETE FROM Users WHERE Username = ?", (username,))
        conn.commit()
    except Exception as e:
        print(f"Failed to remove user '{username}': {str(e)}")
    finally:
        conn.close()


class TestDatabaseMethods(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment before each test.

        This method initializes an in-memory SQLite database and creates necessary tables.
        It also creates a test user for conducting the tests.
        """
        self.conn = sqlite3.connect('userDatabase.db')
        self.cursor = self.conn.cursor()

        # Create tables required for the tests
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Comments (
                        Comment_ID INTEGER PRIMARY KEY,
                        Submission_ID INTEGER,
                        Username TEXT,
                        Comment TEXT
                    )
                ''')

        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Drafts (
                        Draft_ID INTEGER PRIMARY KEY,
                        Username TEXT,
                        Title TEXT,
                        Content TEXT
                    )
                ''')

        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Profiles (
                        Username TEXT PRIMARY KEY,
                        First_Name TEXT,
                        Last_Name TEXT,
                        Email TEXT,
                        Address TEXT
                    )
                ''')

        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Reviews (
                        Submission_ID INTEGER PRIMARY KEY,
                        Username TEXT,
                        Title TEXT,
                        Content TEXT,
                        Rating INTEGER,
                        Accum_Ratings INTEGER,
                        Total_Ratings INTEGER
                    )
                ''')

        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Users (
                        Username TEXT PRIMARY KEY,
                        Password TEXT
                    )
                ''')

        self.conn.commit()

        # Create a test user
        self.test_user = User('test_user', 'password')
        create_user(self.test_user)

    def tearDown(self):
        # Close the database connection and remove the test database
        self.conn.close()
        import os
        os.remove("userDatabase.db")

    def test_create_user(self):
        """
        Test the user creation functionality.

        This test ensures that a user can be successfully created in the database.
        It asserts that the creation returns True and then removes the test user.
        """

        test_user = User("testuser", "testpassword")
        self.assertTrue(create_user(test_user))
        remove_test_user(test_user)



    def test_get_user_data_by_username(self):
        """
        Test retrieving user data by username.

        This test checks whether the 'get_user_data_by_username' function correctly retrieves
        user data for an existing user. It asserts that the retrieved data is not None.
        """

        user = User('test_user', 'password')
        user_created = create_user(user)
        user_data = get_user_data_by_username('test_user')
        self.assertIsNotNone(user_data)
        remove_test_user(user)

    def test_get_user_data_by_nonexistent_username(self):
        """
        Test retrieving user data for a nonexistent username.

        This test ensures that querying a nonexistent username returns None.
        """

        user_data = get_user_data_by_username('nonexistent_user')
        self.assertIsNone(user_data)

    def test_duplicate_user_creation(self):
        """
        Test the creation of a duplicate user.

        This test checks that trying to create a user with a username that already exists in the
        database returns False, indicating the user was not created.
        """
        test_user = User("testuser", "testpassword")
        create_user(test_user)
        self.assertFalse(create_user(test_user))
        remove_test_user(test_user)

    def test_check_credentials(self):
        """
        Test the user credential checking functionality.

        This test verifies that valid credentials return True and invalid credentials
        (both incorrect username and password) return False.
        """

        user = User('test_user', 'password')
        user_created = create_user(user)
        valid_credentials = self.check_credentials('test_user', 'password')
        invalid_credentials = self.check_credentials('nonexistent_user', 'invalid_password')

        self.assertTrue(valid_credentials)
        self.assertFalse(invalid_credentials)
        remove_test_user(self.test_user)

    def test_check_wrong_credentials(self):
        """
        Test checking invalid credentials for an existing user.

        This test ensures that providing a wrong password for an existing user's username
        results in False, indicating invalid credentials.
        """

        user = User('test_user', 'password')
        create_user(user)
        invalid_credentials = self.check_credentials('test_user', 'wrong_password')
        self.assertFalse(invalid_credentials)
        remove_test_user(user)

    def check_credentials(self, user_name, user_password):
        """
        Check if user credentials are valid.

        Args:
            user_name: Username
            user_password: Password

        Returns:
            True if the credentials are valid, otherwise False
        """
        try:
            conn = sqlite3.connect('userDatabase.db')
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM Users WHERE Username=? AND Password=?', (user_name, user_password))
            result = cursor.fetchone()

            conn.close()

            if result is None:
                return False
            else:
                return True
        except Exception as e:
            return False

    def test_publish_review(self):
        """
        Test the retrieval of published reviews.

        This test checks whether the 'get_published_reviews' function correctly retrieves
        all published reviews from the database.
        """

        user = User('test_user', 'password')
        user_created = create_user(user)
        username = 'test_user'
        title = 'Test Title'
        content = 'Test Content'
        publish_review(username, title, content)
        published_reviews = get_published_reviews()

        self.assertTrue(any(title in review[2] for review in published_reviews))

        remove_test_user(self.test_user)



    def test_get_published_reviews(self):
        """
        Test the retrieval of published reviews.

        """
        user = User('test_user', 'password')
        user_created = create_user(user)
        username = 'test_user'
        title = 'Test Title'
        content = 'Test Content'
        publish_review(username, title, content)
        published_reviews = get_published_reviews()
        self.assertIsNotNone(published_reviews)
        remove_test_user(self.test_user)\


    def test_get_comments(self):
        """Test if comments are correctly retrieved for a specific review."""
        submission_id = 1
        username = 'test_user'
        comment = 'This is a test comment.'
        save_comment(submission_id, username, comment)

        retrieved_comments = get_comments(submission_id)
        self.assertEqual(len(retrieved_comments), 1)
        self.assertEqual(retrieved_comments[0][3], comment)

    def test_get_comments_for_review_with_no_comments(self):
        """Verify retrieval of comments for a review that has no comments."""
        submission_id = 2

        retrieved_comments = get_comments(submission_id)
        self.assertEqual(len(retrieved_comments), 0)

    def test_save_comment(self):
        """Check if saving a comment for a specific review functions properly."""
        submission_id = 3
        username = 'test_user'
        comment = 'This is a test comment.'

        save_comment(submission_id, username, comment)

        retrieved_comments = get_comments(submission_id)
        self.assertEqual(len(retrieved_comments), 1)
        self.assertEqual(retrieved_comments[0][3], comment)

    def test_save_multiple_comments_for_same_review(self):
        """Ensure multiple comments can be saved and retrieved for the same review."""
        submission_id = 4
        username = 'test_user'

        comments = ['Comment 1', 'Comment 2', 'Comment 3']

        for comment in comments:
            save_comment(submission_id, username, comment)

        retrieved_comments = get_comments(submission_id)
        self.assertEqual(len(retrieved_comments), len(comments))
        self.assertEqual(retrieved_comments[0][3], comments[0])
        self.assertEqual(retrieved_comments[1][3], comments[1])
        self.assertEqual(retrieved_comments[2][3], comments[2])
    def test_change_password(self):
        """
        Test the password changing functionality for a user.

        This test changes the password of an existing user and then checks if the new password
        is valid and correctly updated in the database.
        """
        change_password('test_user', 'new_password')
        valid = check_credentials('test_user', 'new_password')
        self.assertTrue(valid)

    def test_save_rating(self):
        """Test saving a rating for a review and validating its correct storage."""
        submission_id = 5
        rating = 4

        save_rating(submission_id, rating)

        review_data = get_post_by_id(submission_id)
        self.assertEqual(review_data[4], rating)

    def test_save_multiple_ratings_for_same_review(self):
        """Check if multiple ratings for the same review are correctly averaged and stored."""
        submission_id = 6
        ratings = [5, 3, 4]

        for rating in ratings:
            save_rating(submission_id, rating)

        review_data = get_post_by_id(submission_id)
        self.assertEqual(review_data[4], sum(ratings) // len(ratings))  # Check for correct average rating

    def test_get_users_published_reviews(self):
        """Test retrieving all reviews published by a specific user."""
        username = 'test_user'
        title = 'Test Title'
        content = 'Test Content'
        publish_review(username, title, content)

        published_reviews = get_users_published_reviews(username)
        self.assertEqual(len(published_reviews), 1)
        self.assertEqual(published_reviews[0][2], title)
        self.assertEqual(published_reviews[0][3], content)

    def test_get_users_published_reviews_for_user_with_no_reviews(self):
        """Ensure no reviews are retrieved for a user who hasn't published any."""
        username = 'nonexistent_user'

        published_reviews = get_users_published_reviews(username)
        self.assertEqual(len(published_reviews), 0)



    def test_get_first_name_for_nonexistent_name(self):
        """Verify that searching for a non-existent first name returns no results."""
        non_existent_name = 'Nonexistent'
        users_with_first_name = get_First_Name(non_existent_name)
        self.assertEqual(len(users_with_first_name), 0)




    def test_clear_drafts(self):
        """Confirm that clearing drafts for a user removes all their drafts."""
        username = 'test_user'
        title = 'Draft Title'
        content = 'Draft Content'
        save_draft(username, title, content)

        clear_drafts(username)

        drafts = get_drafts(username)
        self.assertEqual(len(drafts), 0)

    def test_update_post(self):
        """Check updating the title and content of a post and validate the changes."""
        post_id = 1
        original_title = "Original Title"
        original_content = "Original Content"
        new_title = "New Title"
        new_content = "New Content"

        # Insert an initial post with original title and content
        self.cursor.execute("INSERT INTO Reviews (Submission_ID, Username, Title, Content) VALUES (?, ?, ?, ?)",
                            (post_id, 'test_user', original_title, original_content))
        self.conn.commit()

        # Update the post with new title and content
        update_post(post_id, new_title, new_content)

        # Retrieve the updated post data
        updated_post = get_post_by_id(post_id)

        # Check if the post title and content have been updated correctly
        self.assertEqual(updated_post[2], new_title)
        self.assertEqual(updated_post[3], new_content)

    def test_edit_nonexistent_review(self):
        """Test editing a review that does not exist in the database."""
        non_existent_submission_id = 1000
        new_title = 'New Title'
        new_content = 'New Content'

        update_post(non_existent_submission_id, new_title, new_content)

        updated_review = get_post_by_id(non_existent_submission_id)
        self.assertIsNone(updated_review)

    def test_edit_profile(self):
        """
        Test the edit_profile function.

        This test checks whether the 'edit_profile' function correctly updates the profile
        information of an existing user.
        """
        # Create a test user's profile
        test_username = 'test_user'
        new_profile = Profile(test_username)
        new_profile.set_first_name('Turjo')
        new_profile.set_last_name('Paul')
        new_profile.set_email('paul@gmail.com')
        new_profile.set_address('st.Johns')

        # Edit the user's profile
        edit_profile(test_username,new_profile)

        # Retrieve the updated profile data from the database
        updated_profile_data = get_user_data_by_username(test_username)
        print(updated_profile_data)
        # Assert that the profile data has been correctly updated
        self.assertIsNotNone(updated_profile_data)
        self.assertEqual(updated_profile_data[0], test_username)


        # Remove the test user after the test
        remove_test_user(self.test_user)


if __name__ == '__main__':
    unittest.main()

