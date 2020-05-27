import sqlite3

conn = sqlite3.connect('main.db')
c = conn.cursor()
c.execute("SELECT * FROM sqlite_master WHERE type='table' and name='articles'")
if not c.fetchone():
    c.execute('CREATE TABLE articles (id int, title varchar(1024), body text, created datetime)')