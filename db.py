import sqlite3

conn = sqlite3.connect('assessment_details.db')

c = conn.cursor()

# Create table
c.execute('''Drop table assessment''')
c.execute('''CREATE TABLE IF NOT EXISTS assessment

(email text PRIMARY KEY, strength text, employability text)''')
c.execute('''INSERT INTO assessment VALUES ('ajiteshnair@gmail.com','no','no')''')
#c.execute("UPDATE assessment SET employability='no' WHERE email='ajiteshnair@gmail.com' ")
email='raju@gmail.com'
#if None==(c.execute('''SELECT  * from assessment WHERE email = ? ''',(email,)).fetchone()):
#    c.execute('''Insert into assessment values (?,'no','no')''',(email,))
    


#commit the changes to db
print(c.execute('''SELECT  * from assessment ''').fetchall())
conn.commit()

conn.close()

"""
email='ram@hotmail.com'
conn = sqlite3.connect('assessment_details.db')
c = conn.cursor()
print(c.execute('''Select * from assessment''').fetchall())

#c.execute('''Insert into assessment values (?,'no','no')''',(email,))
#print(c.execute('''SELECT  * from assessment WHERE email = ? ''',(email,)).fetchall())
#c.execute("UPDATE assessment SET strength='yes' WHERE email=?", (email,))
#conn.commit()
#print(c.execute('''SELECT  * from assessment WHERE email = ? ''',(email,)).fetchall())
conn.close()

#print(c.execute('''Select * from assessment''').fetchall())
"""
