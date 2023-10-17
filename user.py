from bottle import Bottle, request, run, template, static_file, redirect
import sqlite3, app, database

"""
THIS IS THE DATASTRUCTURE MODEL
"""



# class User:
#     def __init__(self, Username, Password, Title = None, Draft = None):
#         self.username = Username
#         self.password = Password
#         self.title = Title
#         self.draft = Draft
#
#     def set_draft(self, title, draft):
#         self.draft = draft
#
#     def get_draft(self):
#         return self.draft
#
#     def get_user_name(self):
#         return self.username
#
#     def get_password(self):
#         return self.password

class User:
    def __init__(self, Username, Password):
        self.username = Username
        self.password = Password
        self.draft = Draft(None, None)

    def set_draft(self, title, draft):
        self.draft.set_title_and_draft(title, draft)

    def get_draft(self):
        return self.draft.get_title_and_draft()

    def get_user_name(self):
        return self.username

    def get_password(self):
        return self.password


class Draft:
    def __init__(self, Title, Draft):
        self.title = Title
        self.draft = Draft

    def set_title(self, title):
        self.title = title

    def set_daft(self, string):
        self.draft = string

    def set_title_and_draft(self, title, string):
        self.title = title
        self.draft = string

    def get_title(self):
        return self.title

    def get_draft(self):
        return self.draft

    def get_title_and_draft(self):
        return self.title, self.draft
