import sqlite3

def open_db(db='tel_bot.db'):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    return c

def serach_in_table(word, Language='ru'):
    c = open_db()
    word = (word)
    c.execute(f'SELECT * FROM Beginners_kit WHERE {Language}=?', word)
    print(c.fetchone())

def random_answer(limit=4):
    c = open_db()
    c.execute(f'SELECT * FROM kit_starter ORDER BY RANDOM() LIMIT {limit}')
    return c.fetchall()

