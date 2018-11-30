from db import query

def getMessages():
    return query('''
        SELECT text
        FROM messages
        ORDER BY date_created ASC
    ''')

def saveMessage(text):
    query('INSERT INTO messages (text) VALUES (%s)', (text,))
