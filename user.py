
class User:
    """
    Represents a user with a username, password, and draft.
    """

    def __init__(self, username, password):
        """
        Initialize a User instance.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        self.username = username
        self.password = password
        self.draft = Draft(None, None)

    def set_draft(self, title, draft):
        """
        Set the draft title and content.

        Args:
            title (str): The title of the draft.
            draft (str): The content of the draft.
        """
        self.draft.set_title_and_draft(title, draft)

    def get_draft(self):
        """
        Get the title and content of the draft.

        Returns:
            tuple: A tuple containing the title and content of the draft.
        """
        return self.draft.get_title_and_draft()

    def get_user_name(self):
        """
        Get the username of the user.

        Returns:
            str: The username of the user.
        """
        return self.username

    def get_password(self):
        """
        Get the password of the user.

        Returns:
            str: The password of the user.
        """
        return self.password


class Draft:
    """
    Represents a draft with a title and content.
    """

    def __init__(self, title, draft):
        """
        Initialize a Draft instance.

        Args:
            title (str): The title of the draft.
            draft (str): The content of the draft.
        """
        self.title = title
        self.draft = draft

    def set_title(self, title):
        """
        Set the title of the draft.

        Args:
            title (str): The title of the draft.
        """
        self.title = title

    def set_draft(self, string):
        """
        Set the content of the draft.

        Args:
            string (str): The content of the draft.
        """
        self.draft = string

    def set_title_and_draft(self, title, string):
        """
        Set the title and content of the draft.

        Args:
            title (str): The title of the draft.
            string (str): The content of the draft.
        """
        self.title = title
        self.draft = string

    def get_title(self):
        """
        Get the title of the draft.

        Returns:
            str: The title of the draft.
        """
        return self.title

    def get_draft(self):
        """
        Get the content of the draft.

        Returns:
            str: The content of the draft.
        """
        return self.draft

    def get_title_and_draft(self):
        """
        Get the title and content of the draft.

        Returns:
            tuple: A tuple containing the title and content of the draft.
        """
        return self.title, self.draft
