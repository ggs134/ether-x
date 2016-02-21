import sqlite3
import os

con = sqlite3.connect('/home/ggs134/Dropbox/onther/onther/db/development.sqlite3')

cur = con.execute("SELECT name FROM sqlite_master WHERE type='table';")

table=cur.fetchall()

for i in table:
    print i
