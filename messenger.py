from db import query

def saveMessage(text):
    query('INSERT INTO messages (text) VALUES (%s)', (text,))

