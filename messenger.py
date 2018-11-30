from db import query
from google.cloud import translate

translate_client = translate.Client()

def getLanguages():
    return translate_client.get_languages()

def getMessages():
    m = query('''
        SELECT text
        FROM messages
        ORDER BY date_created ASC
    ''')
    x = []
    for i in m:
        x.append(i[0])
    return x

def getMessagesTranslated(lang):
    messages = getMessages()
    messages = translate_client.translate(
        messages,
        target_language=lang
    )
    translatedMessages = []
    for m in messages:
        translatedMessages.append(m['translatedText'])
    print(translatedMessages)
    return translatedMessages

def saveMessage(text):
    language = translate_client.detect_language(text)['language']
    query('''
        INSERT INTO messages (text, language) VALUES (%s, %s)
    ''', (text, language))
