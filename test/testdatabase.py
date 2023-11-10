import unittest

from user import User

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
        """
        self.conn = sqlite3.connect(':memory:')  # Use an in-memory database for testing
        self.cursor = self.conn.cursor()

        # Create tables required for the tests
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT,
                Password TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Reviews (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT,
                Title TEXT,
                Content TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Drafts (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT,
                Title TEXT,
                Content TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Ratings (
                Submission_ID INTEGER,
                Username TEXT,
                Rating INTEGER
            )
        ''')

        self.conn.commit()

        # Create a test user
        self.test_user = User('test_user', 'password')
        create_user(self.test_user)


    def tearDown(self):
        """
        Clean up the test environment after each test.
        """
        try:
            remove_test_user(self.test_user)
        except Exception as e:
            print(f"Failed to clean up: {str(e)}")

        self.conn.close()

    def test_create_user(self):
        test_user = User("testuser", "testpassword")
        self.assertTrue(create_user(test_user))
        remove_test_user(test_user)



    def test_get_user_data_by_username(self):
        """
        Test the 'get_user_data_by_username' method
        """
        user = User('test_user', 'password')
        user_created = create_user(user)
        user_data = get_user_data_by_username('test_user')
        self.assertIsNotNone(user_data)
        remove_test_user(user)

    def test_get_user_data_by_nonexistent_username(self):
        user_data = get_user_data_by_username('nonexistent_user')
        self.assertIsNone(user_data)

    def test_duplicate_user_creation(self):
        test_user = User("testuser", "testpassword")
        create_user(test_user)
        self.assertFalse(create_user(test_user))
        remove_test_user(test_user)

    def test_check_credentials(self):
        """
        Test checking user credentials.
        """
        user = User('test_user', 'password')
        user_created = create_user(user)
        valid_credentials = self.check_credentials('test_user', 'password')
        invalid_credentials = self.check_credentials('nonexistent_user', 'invalid_password')

        self.assertTrue(valid_credentials)
        self.assertFalse(invalid_credentials)
        remove_test_user(self.test_user)

    def test_check_wrong_credentials(self):
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
        Test publishing a review and checking its existence in the retrieved reviews.

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
        remove_test_user(self.test_user)

    def test_change_password(self):
        """
        Test changing a user's password.
        """
        change_password('test_user', 'new_password')
        valid = check_credentials('test_user', 'new_password')
        self.assertTrue(valid)

if __name__ == '__main__':
    unittest.main()

