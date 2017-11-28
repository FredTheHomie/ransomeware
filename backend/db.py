import sqlite3
from util.utils import getUID

db = sqlite3.connect('backend/ccdb.db')
cursor = db.cursor()

def insertToDB(uid, key, paid):
    cursor.execute('''INSERT INTO agents(id, key, paid)
                      VALUES(?, ?, ?)''', (str(uid), key, paid))
    db.commit()
    db.close()


def checkUser(uid):
    cursor.execute('SELECT id FROM agents WHERE id=?', (str(uid),))
    data = cursor.fetchone()
    if data is None:
        return 'no'
    else:
        return 'yes'
    db.close

def checkKey(uid):
    cursor.execute('SELECT key FROM agents WHERE id = ?', (str(uid),))
    data = cursor.fetchone()
    db.close
    return filter(str.isdigit, str(data))
