
from __future__ import print_function
import sqlite3

#connect to db
conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

#drop if have one, create new db
cur.execute('''DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER )''')

#read mbox
fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    # find email addr
    if not line.startswith('From'): continue
    pieces = line.split()
    email = pieces[1]
    # print(email)

    # if in db
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email, ))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts(email, count) VALUES (? , 1)', (email, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, ))

    conn.commit()

# get most frequent 10
for email, count in cur.execute('SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'):
    print(str(email), count)




