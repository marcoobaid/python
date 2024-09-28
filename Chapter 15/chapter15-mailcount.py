# This application will read the mailbox data (mbox.txt) and count the number of email messages 
# per organization (i.e. domain name of the email address) using a database with the 
# following schema to maintain the counts.
#
# CREATE TABLE Counts (org TEXT, count INTEGER)
#
import re
import sqlite3

conn = sqlite3.connect('emailorgdb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fhand = open('mbox.txt')

for line in fhand:
    if not line.startswith('From: '): continue
    org = re.findall(r'@(\S+)', line)[0]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
#sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
   
cur.close()
