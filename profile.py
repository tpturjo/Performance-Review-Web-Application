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
        """
        Get the first name of the user.

        Returns:
            str: The first name of the user.
        """
        return self.first_name

    def get_last_name(self):
        """
        Get the last name of the user.

        Returns:
            str: The last name of the user.
        """
        return self.last_name

    def get_email(self):
        """
        Get the email address of the user.

        Returns:
            str: The email address of the user.
        """
        return self.email

    def get_address(self):
        """
        Get the address of the user.

        Returns:
            str: The physical address of the user.
        """
        return self.address

    def set_first_name(self, name):
        """
        Set the first name of the user.

        Args:
            name (str): The first name to set for the user.
        """
        self.first_name = name

    def set_last_name(self, name):
        """
        Set the last name of the user.

        Args:
            name (str): The last name to set for the user.
        """
        self.last_name = name

    def set_email(self, email):
        """
        Set the email address of the user.

        Args:
            email (str): The email address to set for the user.
        """
        self.email = email

    def set_address(self, address):
        """
        Set the address of the user.

        Args:
            address (str): The physical address to set for the user.
        """
        self.address = address