

import sqlite3

#connects to the database
conn = sqlite3.connect("userDatabase.db")

#Creates the cursor object to interact with the database
cursor = conn.cursor()

#Create table below