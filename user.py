import sqlite3

class User:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def create_account(self, Username, Password):
        # Implement code to insert a new user into the "Users" table
        self.cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?);",
                            (Username, Password))
        self.conn.commit()

    def authenticate(self, Username, Password):
        # Implement code to authenticate the user
        self.cursor.execute("SELECT Username FROM Users WHERE Username = ? AND Password = ?;",
                            (Username, Password))
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False
class Published:
    def __init__(self, Username):
        self.username = Username

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

    def create_draft(self, Username, title, content):
        # Implement code to create a new draft in the "Drafts" table
        self.cursor.execute("INSERT INTO Drafts (Username, Title, Content) VALUES (?, ?, ?);",
                            (Username, title, content))
        self.conn.commit()

    def save_draft(self, draft_id, content):
        # Implement code to update the content of a draft
        self.cursor.execute("UPDATE Drafts SET Content = ? WHERE DraftID = ?;",
                            (content, draft_id))
        self.conn.commit()

    def get_drafts(self, Username):
        # Implement code to retrieve a user's drafts
        self.cursor.execute("SELECT * FROM Drafts WHERE Username = ?;", (Username,))
        drafts = self.cursor.fetchall()
        return drafts

    def close_connection(self):
        self.conn.close()

