from db import query
from google.cloud import translate

translate_client = translate.Client()

def getLanguages():
    return translate_client.get_languages()

def getMessages():
    return query('''
        SELECT text
        FROM messages
        ORDER BY date_created ASC
    ''')

def saveMessage(text):
    query('INSERT INTO messages (text) VALUES (%s)', (text,))
