class Profile:
    """
    Represents a user with a username, password, and draft.
    """

    def __init__(self, username):
        """
        Initialize a User instance.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        self.username = username
        self.first_name = "null"
        self.last_name = "null"
        self.email = "null"
        self.address = "null"


    def get_user_name(self):
        """
        Get the username of the user.

        Returns:
            str: The username of the user.
        """
        return self.username

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

    def set_first_name(self, name):
        self.first_name = name

    def set_last_name(self, name):
        self.last_name = name

    def set_email(self, email):
        self.email = email

    def set_address(self, address):
        self.address = address