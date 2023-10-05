class User:
    """
    A class representing a user.

    Attributes:
    - username (str): the user's username
    - email (str): the user's email address
    - password (str): the user's password
    - group_name (str): the user's group name
    - piece_work (str): the user's piece of work name
    - _user_reviews (str): the user's review

    Methods:
    - set_username(username): sets the user's username
    - get_username(): returns the user's username
    - set_email(email): sets the user's email address
    - get_email(): returns the user's email address
    - set_password(password): sets the user's password
    - get_password(): returns the user's password
    - set_group_name(group_name): sets the user's group name
    - get_group_name(): returns the user's group name
    - set_piece_work(piece_work): sets the user's piece of work name
    - get_piece_work(): returns the user's piece of work name
    - add_user_review(review): adds a review to the user's reviews
    - get_user_reviews(): returns the user's reviews
    """

    def __init__(self, username='', email='', password='********', group_name='',piece_work='',user_review=''):
        self.username = username
        self.email = email
        self.password = password
        self.group_name = group_name
        self.piece_work = piece_work
        self._user_reviews = user_review

    def set_username(self, username):
        """Sets the user's username."""
        self.username = username

    def get_username(self):
        """Returns the user's username."""
        return self.username

    def set_email(self, email):
        """Sets the user's email address."""
        self.email = email

    def get_email(self):
        """Returns the user's email address."""
        return self.email

    def set_password(self, password):
        """Sets the user's password."""
        self.password = password

    def get_password(self):
        """Returns the user's password."""
        return self.password

    def set_group_name(self, group_name):
        """Sets the user's group name."""
        self.group_name = group_name

    def get_group_name(self):
        """Returns the user's group name."""
        return self.group_name

    def set_piece_work(self, piece_work):
        """Sets the user's piece of work name."""
        self.piece_work = piece_work

    def get_piece_work(self):
        """Returns the user's piece of work name."""
        return self.piece_work

    def add_user_review(self, review):
        """Adds a review to the user's reviews."""
        self._user_reviews = review

    def get_user_reviews(self):
        """Returns the user's reviews."""
        return self._user_reviews