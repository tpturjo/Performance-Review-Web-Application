import sqlite3

class User:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.last_user_id = self.get_last_user_id()  # Initialize with the last used UserID

    def get_last_user_id(self):
        # Retrieve the last used UserID from the "Users" table
        self.cursor.execute("SELECT MAX(UserID) FROM Users;")
        result = self.cursor.fetchone()
        if result[0]:
            return result[0]
        else:
            return 0

    def create_account(self, Username, Password):
        # Increment the UserID for the new user
        self.last_user_id += 1
        user_id = self.last_user_id
        # Implement code to insert a new user into the "Users" table
        self.cursor.execute("INSERT INTO Users (UserID, Username, Password) VALUES (?, ?, ?);",
                            (user_id, Username, Password))
        self.conn.commit()

    def authenticate(self, Username, Password):
        # Implement code to authenticate the user
        self.cursor.execute("SELECT UserID FROM Users WHERE Username = ? AND Password = ?;",
                            (Username, Password))
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False
class Published:
    def __init__(self, email, user_name):
        self.__email = email
        self.username = user_name

    def get_email(self):
        return self.__email

    def get_user(self):
        return self.username

    @staticmethod
    def display_reviews(self,database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        all_reviews=self.cursor.fetchall()
        return all_reviews

class Draft:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def create_draft(self, user_id, title, content):
        # Implement code to create a new draft in the "Drafts" table
        self.cursor.execute("INSERT INTO Drafts (UserID, Title, Content) VALUES (?, ?, ?);",
                            (user_id, title, content))
        self.conn.commit()

    def save_draft(self, draft_id, content):
        # Implement code to update the content of a draft
        self.cursor.execute("UPDATE Drafts SET Content = ? WHERE DraftID = ?;",
                            (content, draft_id))
        self.conn.commit()

    def get_drafts(self, user_id):
        # Implement code to retrieve a user's drafts
        self.cursor.execute("SELECT * FROM Drafts WHERE UserID = ?;", (user_id,))
        drafts = self.cursor.fetchall()
        return drafts

    def close_connection(self):
        self.conn.close()
