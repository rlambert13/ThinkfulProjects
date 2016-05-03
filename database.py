# The sqlite3 module is used to work with the SQLite database.
import sqlite3 as lite
import pandas as pd

cities = (('New York City', 'NY'), ('Boston', 'MA'), ('Chicago', 'IL'),
  	('Miami', 'FL'), ('Dallas', 'TX'), ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA'), ('Los Angeles', 'CA'))

weather = (('New York City', 2013, 'July', 'January', 62),
  ('Boston', 2013, 'July', 'January', 59),
  ('Chicago', 2013, 'July', 'January', 59),
  ('Miami', 2013, 'August', 'January', 84),
  ('Dallas', 2013, 'July', 'January', 77),
  ('Seattle', 2013, 'July', 'January', 61),
  ('Portland', 2013, 'July', 'December', 63),
  ('San Francisco', 2013, 'September', 'December', 64),
  ('Los Angeles', 2013, 'September', 'December', 75))

# Here you connect to the database. The `connect()` method returns a connection object.
con = lite.connect('database.db')

with con:
  # From the connection, you get a cursor object. The cursor is what goes over the records that result from a query.
  cur = con.cursor() 

  # Remove tables if they already exist 
  cur.execute('DROP TABLE IF EXISTS cities;')
  cur.execute('DROP TABLE IF EXISTS weather;') 

  # Create tables 
  cur.execute('CREATE TABLE cities (name text, state text);')
  cur.executemany("INSERT INTO cities VALUES(?,?)", cities)

  cur.execute('CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);')
  cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
  
  cur.execute("SELECT name, state FROM cities LEFT OUTER JOIN weather ON weather.city = cities.name WHERE warm_month = 'July';")
  
  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows, columns=cols)

  print("The cities that are warmest in July are: %s" % rows)