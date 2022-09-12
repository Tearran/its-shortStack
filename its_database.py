#!/usr/bin/env python3


import os
import sqlite3
pathis=os.path.dirname(__file__)+'/db/sqlite.db'

try:
    conn = sqlite3.connect(pathis)
  
except Exception as error:
    print(error)

c = conn.cursor()
c.execute("SELECT * FROM its_i2cList")
rows = c.fetchall()

for row in rows:
    print(row)
  
conn.close


