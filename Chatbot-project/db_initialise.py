# This file is only for testing purpose.
# You can initialise values in the db here.

import sqlite3
conn = sqlite3.connect('assessment_details.db')
c = conn.cursor()
c.execute('''Drop table assessment''')
c.execute('''CREATE TABLE IF NOT EXISTS assessment
(email text PRIMARY KEY, strength text, employability text)''')
c.execute('''INSERT INTO assessment VALUES ('receiveremail@gmail.com','yes','no')''')
print(c.execute('''SELECT  * from assessment ''').fetchall())
conn.commit()
conn.close()


