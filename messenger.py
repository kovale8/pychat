from db import query

def getMessages():
    query('''
        SELECT text
        FROM messages
        ORDER BY date_created DESC
    ''')

def saveMessage(text):
    query('INSERT INTO messages (text) VALUES (%s)', (text,))
