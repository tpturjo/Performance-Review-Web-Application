from bottle import Bottle, request, run, template, static_file, redirect
import sqlite3, app, database




class User:
    def __init__(self, Username, Password, Draft = ''):
        self.username = Username
        self.password = Password
        self.set_draft = Draft

    def set_draft(self, draft):
        self.draft = draft

    def get_draft(self):
        return self.draft

    def get_user_name(self):
        return self.username

    def get_password(self):
        return self.password

class Published:
    def __init__(self):
        self.published = []





